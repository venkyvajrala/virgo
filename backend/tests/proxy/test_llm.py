import unittest
import src.proxy.llm as main


class TestLLM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.llm = main.LLM(
            server_url="https://generativelanguage.googleapis.com/v1beta/openai/")

    def test_instance(self):
        self.assertIsInstance(self.llm, main.LLM)

    def test_server_url(self):
        self.assertEqual(
            self.llm.server_url, "https://generativelanguage.googleapis.com/v1beta/openai/")

    def test_client(self):

        def run_test():
            self.assertIsNotNone(self.llm.client().api_key)
            event_stream = self.llm.chat_stream(
                "What's the color of apple?", "gemini-2.0-flash")
            for event in event_stream:
                self.assertIsNotNone(
                    event.to_dict()['choices'][0]['delta']['content'])


if __name__ == "__main__":
    unittest.main()
