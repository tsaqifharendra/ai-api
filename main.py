from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API hidup"}

@app.get("/predict")
def predict():
    return {
        "home": 0.60,
        "draw": 0.22,
        "away": 0.18,
        "decision": "EXECUTE"
    }
