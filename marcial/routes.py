from flask import render_template

from __main__ import app

@app.route("/judo")
def homepage():
    return render_template("judo.html")