import subprocess


def mp3_to_wav(filename: str):
    subprocess.call(['ffmpeg', '-i', './audio.mp3',
                     'audio.wav'])
