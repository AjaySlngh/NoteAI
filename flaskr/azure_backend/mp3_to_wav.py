import subprocess


def mp3_to_wav():
    subprocess.call(['ffmpeg', '-i', 'flaskr/audio.mp3',
                     'flaskr/audio.wav'])
