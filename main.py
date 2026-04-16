from fastapi import FastAPI
from model_loader import load_models

app = FastAPI()

load_models()

@app.get("/")
def root():
    return {"message": "Restaurant API is running!"}