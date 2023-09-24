def write_file():
    file = open("final_summary.txt", "w")
    transcription_file = open("transcription.txt", "r")
    transcription = transcription_file.read()
    file.write(transcription)
    file.close()


def reset_file():
    file = open("transcription.txt", "a")
    file.truncate(0)
    file.close()
