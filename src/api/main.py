from fastapi import FastAPI

app = FastAPI()

products = {
    "cotton t-shirt": "610910",
    "leather shoes": "640399",
    "laptop": "847130",
    "mobile phone": "851713"
}

@app.get("/")
def home():
    return {"message": "HS Code Classification Assistant"}

@app.get("/predict/{product}")
def predict(product: str):
    hs_code = products.get(product.lower())

    if hs_code:
        return {
            "product": product,
            "hs_code": hs_code
        }

    return {
        "error": "Product not found"
    }
