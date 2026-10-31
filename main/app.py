from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

import os

app = Flask(__name__)

@app.route("/home_page")
def home_page():
    return render_template("HomePage.html")