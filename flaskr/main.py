import os
from flask import Flask
from flask import redirect, url_for, render_template, request
import requests
import azure_backend.mp3_to_wav as mp3wav
import azure_backend.abstract_summarize as abstract
import azure_backend.extractive_summary as extract
import azure_backend.transcribe as transcribe
import os
import azure_backend.output as output
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/transcribing', methods=['POST'])
def open_front_page():
    print(request.data)
    mp3wav.mp3_to_wav(request.data)
    transcribe.from_file()
    abstract.sample_abstractive_summarization()
    extract.sample_extractive_summarization(extract.authenticate_client)
    output.write_file()
    output.reset_file()

    return redirect('/display')


@app.route('/display', methods=['GET', 'POST'])
def display_file():
    file = open('final_summary.txt', "r")
    content = file.read()

    print(content)

    return render_template('upload.html', content=content)


@app.route('/ata')
def route_ata():
    return redirect('https://ata.mroley.dev')


@app.route('/upload.html', methods=['GET', 'POST'])
def send_to_uploading():
    print('upload')
    if request.method == 'POST':
        print(request.files)
        file = request.files['filename']
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), f"flaskr/output/{filename}"))
        return requests.post('http://127.0.0.1:5000/transcribing',
                             filename).content

    return render_template('upload.html')


@app.route('/recording.html')
def send_to_recording():
    return render_template('recording.html')
