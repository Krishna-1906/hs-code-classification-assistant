from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
  return ("messages": "HS code classifications assistant is running")
