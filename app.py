from flask import Flask, render_template
import os

app = Flask(__name__, static_folder=os.path.abspath('application/view/static'), template_folder=os.path.abspath('application/view/templates'))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/video/<nomeV>")
def video(nomeV):
    return render_template("video.html", titulo=nomeV)