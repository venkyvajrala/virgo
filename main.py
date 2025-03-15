from fastapi import FastAPI
from src.proxy.llm import LLM
import json

app = FastAPI()


@app.get("/chat/{prompt}")
def gemini_stream_response(prompt: str):
    gemini = LLM("https://generativelanguage.googleapis.com/v1beta/openai/")
    stream = gemini.chat_stream(prompt=prompt, model="gemini-2.0-flash")

    for chunk in stream:
        yield json.dumps(chunk.to_dict()) + "\n"
