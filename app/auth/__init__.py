"""Blueprint for the authentication routes"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import routes
