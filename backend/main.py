from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from fastapi.middleware.cors import CORSMiddleware
from src.proxy.llm import LLM
import json
import asyncio

app = FastAPI()


# Add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/chat/{prompt}")
async def gemini_stream_response(prompt: str):
    gemini = LLM("https://generativelanguage.googleapis.com/v1beta/openai/")
    stream = gemini.chat_stream(prompt=prompt, model="gemini-2.0-flash")

    async def event_generator():
        for chunk in stream:
            yield json.dumps(chunk.to_dict()) + "\n"
            # sleep 1 second
            await asyncio.sleep(1)

    return StreamingResponse(event_generator(), media_type="application/json")
