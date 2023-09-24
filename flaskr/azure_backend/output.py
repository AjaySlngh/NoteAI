def write_file():
    file = open("final_summary.txt", "w")
    file.write("Adaptive Summary: \n")
    abstract_file = open("abstract_summary.txt", "r")
    abstract = abstract_file.read()
    extractive_file = open("extractive_summary.txt", "r")
    extract = extractive_file.read()
    transcription_file = open("transcription.txt", "r")
    transcription = transcription_file.read()
    file.write(abstract)
    file.write("\nExtractive Summary\n")
    file.write(extract)
    file.write("\n\nExact Translation\n")
    file.write(transcription)
    file.close()


def reset_file():
    file = open("transcription.txt", "a")
    file.truncate(0)
    file.close()
