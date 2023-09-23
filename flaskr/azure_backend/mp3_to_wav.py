import subprocess


def mp3_to_wav(filename: str):
    subprocess.call(['ffmpeg', '-i', filename,
                     'audio.wav'])
