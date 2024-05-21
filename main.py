from flask import Flask, render_template, Response, request, send_from_directory
import json
import os

app =Flask(__name__)
app.config['JSON_AS_ASCI'] = False
app.config['SERVER_NAME'] = 'www.applynow.com:8000'

@app.route("style.css")
def styles_css():
    return render_template("styles/styles.css")

app.route("/script.js")
def script_js():
    return render_template("script.js")