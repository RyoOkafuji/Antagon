import importlib.util
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests


def load_cli_module():
    module_path = Path(__file__).resolve().parents[1] / "Antagon Core CLI"
    spec = importlib.util.spec_from_file_location("antagon_core_cli", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AskOllamaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cli_module = load_cli_module()

    @patch("requests.post")
    def test_returns_response_text_on_success(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"response": "ok"}
        mock_post.return_value = mock_response

        result = self.cli_module.ask_ollama("target", "system", "llama3")

        self.assertEqual(result, "ok")

    @patch("requests.post")
    def test_returns_error_message_when_request_fails(self, mock_post):
        mock_post.side_effect = requests.exceptions.ConnectionError("offline")

        result = self.cli_module.ask_ollama("target", "system", "llama3")

        self.assertIn("Ollamaとの通信に失敗しました", result)
        self.assertIn("offline", result)

    @patch("requests.post")
    def test_returns_error_message_when_response_field_is_missing(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"unexpected": "value"}
        mock_post.return_value = mock_response

        result = self.cli_module.ask_ollama("target", "system", "llama3")

        self.assertEqual(result, "Ollamaの応答形式が不正です。'response' フィールドが見つかりません。")

    @patch("requests.post")
    def test_returns_error_message_when_json_decode_fails(self, mock_post):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError("invalid json")
        mock_post.return_value = mock_response

        result = self.cli_module.ask_ollama("target", "system", "llama3")

        self.assertIn("Ollamaとの通信に失敗しました", result)
        self.assertIn("invalid json", result)


if __name__ == "__main__":
    unittest.main()
