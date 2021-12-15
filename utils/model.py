import os
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_URL = "cointegrated/rubert-tiny2-cedr-emotion-detection"
MODEL_DIRECTORY = './models/rubert/'
TOKEN_DIRECTORY = './models/tokenizer/'

list_key = ["no_emotion", "радость", "грусть", "сюрприз", "страх", "гнев"]


def check_models():
    """
    функция проверяет есть ли скачанные модели, и если нет то скачивет и возвращает
    :return: model, tokenizer
    """

    for _, _, files in os.walk(TOKEN_DIRECTORY):
        if len(files) == 1:
            tokenizer = AutoTokenizer.from_pretrained(MODEL_URL)
            tokenizer.save_pretrained(TOKEN_DIRECTORY)
        else:
            tokenizer= AutoTokenizer.from_pretrained(TOKEN_DIRECTORY)

    for _, _, files in os.walk(MODEL_DIRECTORY):
        if len(files) == 1:
            model = AutoModelForSequenceClassification.from_pretrained(MODEL_URL)
            model.save_pretrained(MODEL_DIRECTORY)
        else:
            model= AutoModelForSequenceClassification.from_pretrained(MODEL_DIRECTORY)

    return model, tokenizer


def get_dict(pred):
    # преобразует массив numpy в словарь
    dd = {}
    for i in range(len(pred[0])):
        dd[list_key[i]] = pred[0][i]
    return dd


def get_models():

    tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2-cedr-emotion-detection")
    model = AutoModelForSequenceClassification.from_pretrained("cointegrated/rubert-tiny2-cedr-emotion-detection")
    return model, tokenizer


@torch.no_grad()
def predict(text, model, tokenizer):
    #функция прогнозирует текст
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1).tolist()

    return np.array(predicted)