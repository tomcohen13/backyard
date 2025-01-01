from flask import redirect, render_template, url_for
from . import main

@main.route('/')
def index():
    return redirect(url_for('auth.login'))
    return "Welcome to the main page!"

@main.route('/about')
def about():
    return render_template("about.html")