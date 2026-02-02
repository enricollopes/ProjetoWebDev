from flask import render_template, url_for, redirect, session

from marcial import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/boxe")
def boxe():
    return render_template("boxe.html")


@app.route("/jiu-jitsu")
def jj():
    return render_template("jj.html")

@app.route("/judo")
def judo():
    return render_template("judo.html")

@app.route("/thai")
def thai():
    return render_template("thai.html")