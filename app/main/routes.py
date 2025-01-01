from flask import redirect, render_template, url_for
from . import main

@main.route('/')
def index():
    return redirect(url_for('auth.gate'))

@main.route('/about')
def about():
    return render_template("about.html")


@main.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@main.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@main.app_errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html'), 403