from openspeechcorpus_cli.utils import get_all_text_transcriptions_with_file_name
from openspeechcorpus_cli.utils.common_filters import extract_phones_from_word


def execute_script(transcription_file, output_file, phonetic_annotator=extract_phones_from_word):
    transcriptions = get_all_text_transcriptions_with_file_name(transcription_file)
    output_file = open(output_file, 'w+')
    output_file.write("#!MLF!#\n")
    for file_name, transcription in transcriptions:
        output_file.write(f'"*/{file_name}.lab"\n')
        for word in transcription.split():
            output_file.write("sil\n")
            for phoneme in phonetic_annotator(word):
                if phoneme.replace(" ", ""):
                    output_file.write(f"{phoneme}\n")
            output_file.write("sil\n")
        output_file.write(".\n")

    output_file.close()

