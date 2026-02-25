from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

@app.get("/llm{prompt}")
async def read_root(prompt):
#Crear una logica que me permita comunicarme con un LLM 
    from google import genai

    
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3.1-pro-preview", contents=prompt
    )
    print(response.text)

    return {"Respuesta": response.text}

