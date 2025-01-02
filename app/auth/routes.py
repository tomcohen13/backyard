"""Routes for the authentication blueprint"""
from flask import flash, redirect, render_template, url_for

from . import auth


def flash_error():
    flash("There was an error, please try again later", "error-message")

@auth.route('/', methods=["GET"])
def gate():
    return render_template("auth/gate.html")

@auth.route('/signin', methods=["POST"])
def signin():
    flash("Invalid credentials 🤷", "error-message")
    return redirect(url_for("auth.gate"))

@auth.route('/signup', methods = ["POST"])
def signup():
    flash("We're currently not accepting new users. Try again later!", "error-message")
    return redirect(url_for("auth.gate"))

@auth.route('/reset', methods = ["POST"])
def reset():
    flash_error()
    return redirect(url_for("auth.gate"))