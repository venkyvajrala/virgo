from openai import OpenAI
import os


class LLM:
    def __init__(self, server_url: str, system_prompt: str | None = "You are a helpful assistant."):
        self.server_url = server_url
        self.system_prompt = system_prompt

    def client(self):
        if (os.environ.get("OPENAI_API_KEY")):
            return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=self.server_url)
        else:
            raise Exception(
                "OPENAI_API_KEY not found in environment variables")

    def chat_stream(self, prompt: str, model: str):

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

        for event in stream:
            yield event
