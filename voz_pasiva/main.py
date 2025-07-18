import spacy
from fastapi import FastAPI
from spacy.matcher import DependencyMatcher

app = FastAPI()

@app.get("/voz_pasiva")
def identificar_voz_pasiva(texto:str):
    if utiliza_voz_pasiva(texto):
        return "Se utiliza voz pasiva"
    else:
        return "No se utiliza voz pasiva"

def utiliza_voz_pasiva(texto: str):
    doc = nlp(texto)
    coincidencias = matcher(doc)
    if coincidencias:
        return True
    else:
        return False

def obtener_patron_voz_pasiva_canonica():
    return [
        {
            "RIGHT_ID": "verbo_participio",
            "RIGHT_ATTRS": {"POS": "VERB", "DEP": "ROOT"}
        },
        {
            "LEFT_ID": "verbo_participio",
            "REL_OP": ">",
            "RIGHT_ID": "forma_verbal_de_ser",
            "RIGHT_ATTRS": {"POS": "AUX", "DEP": "aux", "LEMMA": "ser"}
        },
        {
            "LEFT_ID": "verbo_participio",
            "REL_OP": ">",
            "RIGHT_ID": "sujeto",
            "RIGHT_ATTRS": {"POS": "NOUN", "DEP": "nsubj"}
        }
    ]

def obtener_patron_voz_pasiva_refleja():
    return [
        {
            "RIGHT_ID": "verbo_en_tercera_persona",
            "RIGHT_ATTRS": {"POS": "VERB", "DEP": "ROOT"}
        },
        {
            "LEFT_ID": "verbo_en_tercera_persona",
            "REL_OP": ">",
            "RIGHT_ID": "palabra_se",
            "RIGHT_ATTRS": {"POS": "PRON", "LOWER": "se", "DEP": "expl:pass"}
        },
        {
            "LEFT_ID": "verbo_en_tercera_persona",
            "REL_OP": ">",
            "RIGHT_ID": "sujeto",
            "RIGHT_ATTRS": {"POS": "NOUN", "DEP": "nsubj"}
        }
    ]

def obtener_patron_voz_pasiva_con_dativo():
    return [
        {
            "RIGHT_ID": "verbo_participio",
            "RIGHT_ATTRS": {"POS": "VERB", "DEP": "ROOT"}
        },
        {
            "LEFT_ID": "verbo_participio",
            "REL_OP": ">",
            "RIGHT_ID": "complemento_indirecto",
            "RIGHT_ATTRS": {"POS": "PRON", "DEP": {"IN": ["iobj", "obj"]}}
        },
        {
            "LEFT_ID": "verbo_participio",
            "REL_OP": ">",
            "RIGHT_ID": "forma_verbal_de_ser",
            "RIGHT_ATTRS": {"POS":"AUX", "DEP": "aux", "LEMMA": "ser"}
        },
        {
            "LEFT_ID": "verbo_participio",
            "REL_OP": ">",
            "RIGHT_ID": "sujeto",
            "RIGHT_ATTRS": {"POS": "NOUN", "DEP": {"IN": ["nsubj", "obj"]}}
        }
    ]

nlp = spacy.load("es_dep_news_trf")
matcher = DependencyMatcher(nlp.vocab)

patron = obtener_patron_voz_pasiva_canonica()
matcher.add("VOZ_PASIVA_CANONICA", [patron])

patron = obtener_patron_voz_pasiva_refleja()
matcher.add("VOZ_PASIVA_REFLEJA", [patron])

patron = obtener_patron_voz_pasiva_con_dativo()
matcher.add("VOZ_PASIVA_CON_DATIVO", [patron])