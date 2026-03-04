from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

# Servir archivos estáticos desde la carpeta `static`
app.mount("/static", StaticFiles(directory="static"), name="static")


class PromptIn(BaseModel):
    prompt: str
    model: str = "gemini-3-flash-preview"


@app.post("/api/llm")
async def llm_api(payload: PromptIn):
    # Lógica mínima para comunicar con el LLM (usa la misma librería que tenías)
    try:
        from google import genai

        client = genai.Client()

        response = client.models.generate_content(
            model=payload.model, contents=payload.prompt
        )

        # Dependiendo de la versión, `response` puede variar. Intentamos usar `.text`.
        text = getattr(response, "text", None)
        if text is None:
            # intento alternativo si la respuesta tiene otra estructura
            text = str(response)

        return JSONResponse({"respuesta": text})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/")
async def root():
    return FileResponse("static/index.html")

