from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/roll-d20")
def roll_d20():
    return {"result": random.randint(1, 20)}