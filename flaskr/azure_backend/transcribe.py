import os
import time
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription=os.environ.get(
    'SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

src_filename = "president_speech.mp3"
dest_filename = "president_speech.wav"

file = open('transcription.txt', 'a')
file.truncate(0)


def from_file():
    audio_input = speechsdk.AudioConfig(filename="president_speech.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_input, language="en-US"
    )

    speech_recognizer.start_continuous_recognition()

    done = False

    def on_recognized(evt):
        assert (
            evt.result.reason == speechsdk.ResultReason.RecognizedSpeech
        ), "A portion was not recognized."
        print("RECOGNIZED: {}".format(evt.result.text))
        file.write(evt.result.text)
        file.write("\n")

    def stop_cb(evt):
        print("CLOSING on {}".format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    speech_recognizer.recognized.connect(on_recognized)
    speech_recognizer.session_stopped.connect(stop_cb)

    while not done:
        time.sleep(.5)


from_file()
file.close()
