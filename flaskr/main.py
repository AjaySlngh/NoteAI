from flask import Flask
from flask import redirect, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def open_front_page():
    return render_template('frontPage.html', name='Ata')

@app.route('/ata')
def route_ata():
    return redirect('https://ata.mroley.dev')

@app.route('/recording')
def send_to_recording():
    return render_template('recording.html')



