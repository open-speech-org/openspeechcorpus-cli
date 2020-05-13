

def get_all_text_transcriptions(transcription_file):
    with open(transcription_file) as file:
        lines = file.readlines()
        return [" ".join(line.split(",")[1:]).lower() for line in lines]
