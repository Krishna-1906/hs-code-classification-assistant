from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load CSV
df = pd.read_csv("data/sample_hs_codes.csv")
print(df)
print(df.columns.tolist())

@app.get("/")
def home():
    return {
        "message": "HS Code Classification Assistant"
    }

@app.get("/predict/{product}")
def predict(product: str):

    result = df[df["product"].str.lower() == product.lower()]

    if not result.empty:
        return {
            "product": product,
            "hs_code": str(result.iloc[0]["hs_code"])
        }

    return {
        "error": "Product not found"
    }
