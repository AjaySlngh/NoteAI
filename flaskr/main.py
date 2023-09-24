import os
from flask import Flask
from flask import redirect, url_for, render_template, request
import requests
import azure_backend.mp3_to_wav as mp3wav
import azure_backend.abstract_summarize as abstract
import azure_backend.extractive_summary as extract
import azure_backend.transcribe as transcribe
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/transcribing', methods=['POST'])
def open_front_page():
    mp3wav.mp3_to_wav("elevator.mp3")
    transcribe.from_file()
    abstract.sample_abstractive_summarization()
    extract.sample_extractive_summarization(extract.authenticate_client)
    text = ''

    return text


@app.route('/display', methods=['GET', 'POST'])
def display_file():
    file = open('transcription.txt', "r")
    content = file.read()

    return render_template('upload.html', content=content)


@app.route('/ata')
def route_ata():
    return redirect('https://ata.mroley.dev')


@app.route('/upload.html', methods=['GET', 'POST'])
def send_to_uploading():
    if request.method == 'POST':
        print(request.files)
        file = request.files['filename']
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), f"flaskr/output/{filename}"))
    return render_template('upload.html')


@app.route('/recording.html')
def send_to_recording():
    return render_template('recording.html')
