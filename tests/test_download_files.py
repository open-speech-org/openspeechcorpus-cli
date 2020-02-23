import unittest

from unittest import mock, TestCase


class DownloadFiles(TestCase):

    @mock.patch("requests.get")
    def test_download_single_url_sucessfull(self, mock_requests):
        mock_requests.return_value.status_code = True
        mock_requests.return_value.json.return_value = []

