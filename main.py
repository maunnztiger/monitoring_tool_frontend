from flask import Flask, render_template, Response, request, send_from_directory
import json
import os

app =Flask(__name__)
app.config['JSON_AS_ASCI'] = False
app.config['SERVER_NAME'] = 'www.tamama.com:8000'

@app.route("/style.css")
def styles_css():
    return render_template("styles/styles.css")

app.route("/script.js")
def script_js():
    return render_template("script.js")

@app.route("/")
def hellou():
    return render_template("login_page.html")

@app.route("/<string:page>")
def data_html(page):  
   return render_template(str(page))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == '__main__':
    app.run(host="www.tamama.com", port=8000, debug=True)