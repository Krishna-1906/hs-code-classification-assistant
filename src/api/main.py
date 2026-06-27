from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.get("/")
def home():
    return {"message": "HS Code Classification Assistant"}

@app.get("/predict/{product}")
def predict(product: str):

    prompt = f"""
You are an expert in HS Code Classification.

Classify this product:

{product}

Return ONLY JSON in this format:

{{
  "product":"{product}",
  "hs_code":"XXXXXX",
  "reason":"short reason"
}}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()
