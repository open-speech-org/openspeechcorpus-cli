#!/usr/bin/env python

import os
import argparse

from openspeechcorpus_cli.utils import execute_script_with_args_if_file_does_not_exists


from openspeechcorpus_cli.htk import (
    generate_isolated_words_grammar,
    generate_list_words,
)


def execute_from_command_line():
    parser = argparse.ArgumentParser(
        "Configure HTK configuration files"
    )

    parser.add_argument(
        "project_name",
        help="Name of the HTK project"
    )

    parser.add_argument(
        "--transcription_file",
        default="transcription.txt",
        help="Name of the transcription file, this file must be a file where each line contains the relative path to a"
             "recording and the transcription of that recording, the separation for the two args must be a comma"
    )

    parser.add_argument(
        "--project_folder",
        default="htk_config",
        help="etc folder for Sphinx train"
    )

    args = vars(parser.parse_args())

    project_name = args["project_name"]
    transcript_file = args["transcription_file"]
    project_folder_name = args["project_folder"]
    test_size = args["test_size"]
    ignore_wav_missing = args.get("ignore_wav_missing", False)
    # Configuration Folder
    if not os.path.exists(project_folder_name):
        print("Creating project folder")
        os.makedirs(project_folder_name)
        print("project folder created")
    else:
        print("Project folder already created, skipping")

    generate_list_words.execute_script(transcript_file, f"{project_name}.words_sorted.list")

    generate_isolated_words_grammar.execute_script(transcript_file, f"{project_name}.words_grammar")
