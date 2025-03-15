"""
This module provides the LLM class to interact with the OpenAI API for generating chat completions.
"""

import os
from openai import OpenAI


class LLM:
    """
    A class to interact with OpenAPI API for generating chat completions
    """

    def __init__(self, server_url: str, system_prompt: str | None = "You are a helpful assistant."):
        """
        Intialize the LLM class with the server_url and system_prompt
        """
        self.server_url = server_url
        self.system_prompt = system_prompt

    def client(self):
        """
        Create and return an OpenAI client
        """
        if os.environ.get("OPENAI_API_KEY"):
            return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=self.server_url)

        raise RuntimeError(
            "OPENAI_API_KEY not found in environment variables")

    def chat_stream(self, prompt: str, model: str):
        """
        Generate a stream of chat completions for the given prompt and model.
        """
        client = self.client()
        stream = client.chat.completions.create(
            model=model,
            n=1,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )

        yield from stream
