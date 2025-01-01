# Import flask dependencies
from flask import render_template

from . import auth

# @auth.route("/", methods=["GET"])
# def gate():
#     return render_template("auth/gate.html")

@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template("auth/gate.html")

@auth.route('/signup', methods = ["POST"])
def signup():
    return render_template("auth/gate.html")

@auth.route('/reset', methods = ["POST"])
def reset_pwd():
    return render_template("auth/gate.html")