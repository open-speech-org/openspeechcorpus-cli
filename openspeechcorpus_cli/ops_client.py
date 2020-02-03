import logging
import os

import requests

from openspeechcorpus_cli.utils import download_file

LOGGER = logging.getLogger(__name__)


class OPSClient (object):
    """
    Open Speech Corpus Client
    """
    _corpus = None
    _base_url = None
    _text_node = None
    _s3_prefix = None
    _output_folder = None
    _output_file = None

    def __init__(
            self,
            corpus,
            extra_query_params,
            output_folder,
            output_file
    ):
        if corpus:
            if corpus == "tales":
                self._corpus = corpus
                self._base_url = "http://openspeechcorpus.contraslash.com/api/tale-sentences/list/"
                self._text_node = "tale_sentence"
                self._s3_prefix = "https://s3.amazonaws.com/contraslash/openspeechcorpus"
            elif corpus == "aphasia":
                self._corpus = corpus
                self._base_url = "http://openspeechcorpus.contraslash.com/api/words/list/"
                self._text_node = "level_sentence"

            elif corpus == "words":
                self._corpus = corpus
                self._base_url = "http://openspeechcorpus.contraslash.com/api/isolated-words/list/"
                self._text_node = "isolated_word"

            else:
                LOGGER.error("Unexisting corpus, valid options are: tales, aphasia, words, raising exception")
                raise ValueError("Unexisting corpus, valid options are: tales, aphasia, words")
            LOGGER.info(f"{self._corpus.capitalize()} corpus selected, using URL: {self._base_url}")
        else:
            LOGGER.error("Specify a valid corpus, raising exception")
            raise ValueError("Specify a valid corpus")

        self._output_folder = output_folder
        self._output_file = output_file

    def _process_single_url(self, extra_url_params=""):
        response = requests.get(f"{self._base_url}?{extra_url_params}")
        if response.status_code == 200:
            json_data = response.json()
            LOGGER.info("We get {} audio datas".format(len(json_data)))
            LOGGER.debug(json_data)
            self._download_files(json_data)
        else:
            LOGGER.info("Cannot connect to server, response status was {}".format(response.status_code))

    def _download_files(self, json_data):
        for audio_data in json_data:
            LOGGER.info("Element: {}".format(audio_data["id"]))
            if self._corpus == "tales":
                audio_id = audio_data["audio"]["audiofile"].replace(".mp4", "")
                file_name = "{}.mp4".format(os.path.join(self._output_folder, str(audio_data["audio"]["id"])))
            else:
                audio_id = audio_data["audio"]["id"]
                file_name = "{}.mp4".format(os.path.join(self._output_folder, str(audio_id)))
            self._output_file.write("{},{}\n".format(file_name, audio_data[self._text_node]["text"].strip()))
            if not os.path.exists(file_name):
                LOGGER.info("Download file: {}{}.mp4".format(self._s3_prefix, audio_id))
                LOGGER.info("Saving into {}".format(file_name))
                try:
                    download_file(
                        "{}{}.mp4".format(self._s3_prefix, audio_id),
                        file_name
                    )
                except ConnectionError:
                    LOGGER.error("Error getting file {}".format(file_name))
            else:
                LOGGER.info("File {} already exists, skipping".format(file_name))

    def download_with_extra_query_params(self, extra_query_params):
        """
        Download using the specified query params
        """
        LOGGER.info(f"Downloading with extra params: {extra_query_params}")
        self._process_single_url(extra_query_params)


    def download_all(self, _from=1):
        pass


