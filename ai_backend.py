from fastapi import APIRouter
from pydantic import BaseModel
import openai
import os

router = APIRouter()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Pergunta(BaseModel):
    pergunta: str

@router.post("/perguntar")
def responder(pergunta: Pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": pergunta.pergunta}
        ]
    )
    return {"resposta": resposta.choices[0].message.content}