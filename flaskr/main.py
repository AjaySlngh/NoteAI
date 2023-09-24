from flask import Flask
from flask import redirect, url_for, render_template, request
import requests
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def open_front_page():
    return render_template('frontPage.html', name='Ata')

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
