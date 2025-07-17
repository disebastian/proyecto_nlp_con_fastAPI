# Proyecto: Servicio Web con FastAPI para Procesamiento de Lenguaje Natural

Este repositorio contiene un servicio web básico desarrollado con **FastAPI**, diseñado para gestionar funcionalidades de **procesamiento de lenguaje natural (NLP)**. El sistema permite:

- Identificar adverbios
- Identificar voz pasiva
- Identificar oraciones largas

El objetivo es ofrecer una base funcional para experimentar con técnicas de NLP aplicadas a problemas prácticos de análisis de texto.

---

## Requisitos

- Python 3.8 o superior
- [Spacy](https://spacy.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- (Opcional) Entorno virtual con `venv`

---

## Instalación

1. Cloná este repositorio:

   ```bash
   git clone git@github.com:disebastian/proyecto_nlp_con_fastAPI.git
   cd proyecto_nlp_con_fastAPI
   ```

2. Creá y activá un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv entornoFastApi
   source entornoFastApi/bin/activate  # En Linux/Mac
   entornoFastApi\Scripts\activate     # En Windows
   ```

3. Instalá las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecutar el servicio

Con el entorno virtual activado y dentro de la carpeta del servicio que te interese usar, ejecutá:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor en:

```
http://127.0.0.1:8000
```

---

## Probando el servicio

Una vez que el servicio esté en funcionamiento, podés verificar que responde correctamente utilizando la documentación automática que ofrece FastAPI.

### Interfaces de documentación generadas automáticamente

FastAPI genera dos interfaces de documentación interactivas:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Ambas muestran una descripción automática de todas las rutas disponibles en tu API, los parámetros que acepta y cómo es la respuesta esperada.

### Usar Swagger UI para probar los endpoints

1. Ingresá a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Buscá el endpoint del servicio que vas a usar
3. Hacé clic en **"Try it out"**
4. Ingresá los datos solicitados (por ejemplo, una palabra o texto)
5. Hacé clic en **"Execute"**
6. Verás la respuesta JSON justo debajo, junto con los detalles de la solicitud enviada
