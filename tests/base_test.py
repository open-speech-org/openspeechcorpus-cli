from unittest import TestCase

OPS_URL = "http://openspeechcorpus.contraslash.com/"


class BaseTest(TestCase):

    def setUp(self) -> None:
        self.ops_url = OPS_URL
