from fastapi import FastAPI
from utils.model import get_models, predict, get_dict, check_models
import uvicorn

app = FastAPI()

# model, tokenizer = get_models()
model, tokenizer = check_models()

#label_codes={0: "no_emotion", 1: "радость", 2: "грусть", 3: "сюрприз", 4: "страх", 5: "гнев"}

@app.get("/emotion-detection/{text}")
async def emotion_detection(text):
    ###   Return emotion detection    ###
    result = predict(text, model, tokenizer)
    result = get_dict(result)

    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload = True)
