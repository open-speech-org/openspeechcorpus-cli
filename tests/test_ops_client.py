from tests.base_test import BaseTest

from openspeechcorpus_cli.ops_client import OPSClient

class TestOPSClient(BaseTest):

    def setUp(self) -> None:
        self.ops_client = OPSClient()