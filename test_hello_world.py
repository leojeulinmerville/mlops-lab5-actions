import unittest

from hello_world import app, greet, generate_html


class HelloWorldTests(unittest.TestCase):
    def setUp(self) -> None:
        app.testing = True
        self.client = app.test_client()

    def test_greet_returns_expected_message(self) -> None:
        expected = "Welcome to CI/CD 101 using GitHub Actions!"
        self.assertEqual(greet(), expected)

    def test_generate_html_includes_message(self) -> None:
        message = "Test message"
        html = generate_html(message)
        self.assertIn(message, html)

    def test_greeting_endpoint_status_code(self) -> None:
        response = self.client.get("/greeting")
        self.assertEqual(response.status_code, 200)

    def test_greeting_endpoint_contains_message(self) -> None:
        response = self.client.get("/greeting")
        body = response.get_data(as_text=True)
        self.assertIn(greet(), body)


if __name__ == "__main__":
    unittest.main()
