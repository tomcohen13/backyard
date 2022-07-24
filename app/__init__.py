# Import flask and template operators
from flask import Flask, render_template, session

# Import environment stuff
import os
from dotenv import load_dotenv
load_dotenv()

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import Talisman
from flask_talisman import Talisman

# Import Mail Stuff
from flask_mail import Mail
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_pyfile('../config.py')

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["CSRF_SESSION_KEY"] = os.environ["CSRF_SESSION_KEY"]

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Secure App with Talisman
Talisman(app, content_security_policy=None)

# Mail Service
mail = Mail(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def no(error):
    return render_template('403.html'), 403

# Import a module / component using its blueprint handler variable (mod_auth)
from app.auth.routes import auth as auth_module
from app.admin.routes import admin as admin_module
from app.mail.routes import mail as mail_module

# Register blueprints
app.register_blueprint(auth_module)
app.register_blueprint(admin_module)
app.register_blueprint(mail_module)

# Build the database:
# This will create the database file using SQLAlchemy
# db.drop_all()
db.create_all()
