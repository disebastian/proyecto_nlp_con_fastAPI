import re
from fastapi import FastAPI

app = FastAPI()

""" 
    \b            # límite de palabra
    \w+           # al menos una letra o dígito
    (?:[-.@]\w+)* # guion, punto, arroba (etc), seguido de letras/dígitos, repetido cero o más
    \b            # límite de palabra 
"""

@app.get("/oraciones_largas/")
def oraciones_largas(texto: str):
    textoLimpio = re.findall(r'\b\w+(?:[-.@]\w+)*\b', texto)
    cantPalabras = len(textoLimpio)
    if cantPalabras > 25:
        return "Es una oración larga, tiene más de 25 palabras."
    else:
        return "No es una oración larga, tiene 25 palabras o menos."
