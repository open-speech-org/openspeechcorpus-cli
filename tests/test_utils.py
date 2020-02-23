from unittest import mock

from openspeechcorpus_cli.utils import download_file

from tests.base_test import BaseTest


class TestUtils(BaseTest):

    @mock.patch('requests.get')
    def test_download_file_good_response(self, requests_get):
        requests_get.return_value.iter_content.return_value = [b'bla']
        mock_open = mock.mock_open()
        with mock.patch('builtins.open', mock_open):
            download_file(self.ops_url, "tmp_file.wav")
        print(mock_open.mock_calls)
        print(";;;;;;")
