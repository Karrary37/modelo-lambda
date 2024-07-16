import unittest
import json
from handler import hello


class TestHelloFunction(unittest.TestCase):
    def test_hello(self):
        event = {}
        context = {}
        response = hello(event, context)

        self.assertEqual(response["statusCode"], 200)
        body = json.loads(response["body"])
        self.assertEqual(body["message"], "Hello, World!")
        self.assertEqual(body["input"], event)

    def test_hello_with_event(self):
        event = {"key": "value"}
        context = {}
        response = hello(event, context)

        self.assertEqual(response["statusCode"], 100)
        body = json.loads(response["body"])
        self.assertEqual(body["message"], "Hello, World!")
        self.assertEqual(body["input"], event)
