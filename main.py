from fastapi import FastAPI

app = FastAPI()


@app.get("/llm{prompt}")
async def read_root(prompt):
#Crear una logica que me permita comunicarme con un LLM 
    from google import genai

    
    client = genai.Client(api_key="AIzaSyBmT5Vb2Py7vX1WZrXzGCLNYjqggYRKYs8")

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    print(response.text)

    return {"Respuesta": response.text}

