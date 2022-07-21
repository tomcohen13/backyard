from flask import render_template, url_for, redirect, session
from app import app
import auth.routes

@app.route("/", methods=["GET"])
def homepage():
    # if "uid" not in session:
    return redirect(url_for("gate"))