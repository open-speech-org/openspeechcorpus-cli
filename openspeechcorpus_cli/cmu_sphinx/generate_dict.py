#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Crea un diccionario a partir de una lista de fonemas
"""
import codecs
import re
from openspeechcorpus_cli.cmu_sphinx.common_filters import *


def execute_script(transcript_file, output_dict):
    words = []
    word_phones = []
    file = codecs.open(transcript_file, 'r', encoding="UTF-8")
    lines = file.readlines()

    for line in lines:
        line = " ".join(line.split(",")[1:]).lower()
        # line_words = re.split(':|;|\.| |,|-|\n|\r|\(|\)|¿|\?|¡|!', line)
        line_words = re.split('[:; ,\n\r()¿¡!]', ' '.join(line.replace("&quot;", " ").split(".")))

        for word in line_words:
            word = apply_filters(word)
            if word not in words:
                words.append(word)
                word_phones.append(extract_phones_from_word(word))

    output_file = codecs.open(output_dict, 'w+', encoding="UTF-8")
    for i in range(len(words)):
        output_file.write(str(words[i]) + " " + str(word_phones[i]) + "\n")

    output_file.close()
