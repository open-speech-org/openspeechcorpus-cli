#!/bin/bash
NAME=$1

DB_NAME="etc/"${NAME}
echo ${DB_NAME}
PWD=$(pwd)
DB_FOLDER=${NAME}"/"${NAME}


python generate_lm_transcription.py
text2wfreq < ${DB_NAME}.transcription | wfreq2vocab > ${DB_NAME}.vocab
text2idngram -vocab ${DB_NAME}.vocab -idngram ${DB_NAME}.idngram < ${DB_NAME}.transcription
idngram2lm -vocab_type 0 -idngram ${DB_NAME}.idngram -vocab ${DB_NAME}.vocab -arpa ${DB_NAME}.lm
sphinx_lm_convert -i ${DB_NAME}.lm -o ${DB_NAME}.lm.DMP
