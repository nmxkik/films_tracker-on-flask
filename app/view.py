from app import app
from flask import render_template



@app.route("/films")
def films():
    return render_template("films.html")

@app.route("/cartoons.html")
def cartoons():
    return render_template("cartoons.html")

@app.route("/tvseries")
def tvseries():
    return render_template("tvseries.html")

@app.route("/anime.html")
def anime():
    return render_template("anime.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
   