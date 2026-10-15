"""Simple automated tests for the rule-based chatbot."""

import unittest
from unittest.mock import patch

from chatbot import get_response


class ChatbotTests(unittest.TestCase):
    def test_greeting(self):
        response = get_response("hello")
        self.assertTrue(any(word in response.lower() for word in ("hello", "hi", "hey")))

    def test_name(self):
        self.assertIn("DecodeBot", get_response("what is your name"))

    def test_help(self):
        self.assertIn("bye", get_response("help").lower())

    def test_blank_message(self):
        self.assertIn("type a message", get_response(""))

    def test_ai_explanation(self):
        self.assertIn("Artificial Intelligence", get_response("what is AI"))

    def test_unknown_message(self):
        self.assertIn("not sure", get_response("what is the meaning of life").lower())


if __name__ == "__main__":
    unittest.main()
