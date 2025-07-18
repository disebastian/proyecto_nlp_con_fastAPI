import spacy
from fastapi import FastAPI
app = FastAPI()

@app.get("/adverbios")
def identificar_adverbios(texto:str):
    #nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    return [token.text for token in doc if token.pos_ == "ADV"]

nlp = spacy.load("es_core_news_sm")