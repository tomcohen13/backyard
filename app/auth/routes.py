# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.auth.forms import LoginForm, SignupForm
from app.auth.helper import *

# Import data models
from app.models import Institution, User

from app.routes import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route("/", methods=["GET"])
def gate():
    
    return render_template("auth/gate.html")

@auth.route('/signin', methods=['POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate():

        user = User.query.filter_by(email=form.email.data).first()
        if not user:

            flash("You need to sign up first!", 'error-message')
            return render_template("auth/gate.html", revealed = True)

        if check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id
            session.permanent = True
            
            return redirect(url_for('index'))

        flash('Mmmm not the password I got..!', 'error-message')
    
    flash("Can't seem to read that email...", 'error-message')

    return render_template("auth/gate.html", revealed = True)

@auth.route('/signup', methods = ["POST"])
def signup():
    
    form = SignupForm(request.form)

    if form.validate():
        
        ### Add another check: if the user is in the db but is unverified, allow to sign up. 
        if User.query.filter_by(email=form.email.data).first():

            flash("You're already registered!", 'error-message')
            
            return render_template("auth/gate.html", revealed = True)

        institution_id = email_to_institution_id(form.email.data)
        
        name = scrape_name(form.email.data)

        if not institution_id:
            flash("Bummer, but your institution isn't in the Backyard yet. Let's change that!", category = "error-message")

            return render_template("auth/gate.html", revealed = True)
        
        new_user = User(email = form.email.data, 
                        password = generate_password_hash(form.password.data), 
                        name = name,
                        institution_id=institution_id,
                        )

        if new_user.register():

            flash("Success! Check your inbox to verify your account", category = "success-message")

            return render_template("auth/gate.html", revealed = True)
            
        else:
            flash("There was a problem signing you up. Try again later!", category = "error-message")

        return render_template("auth/gate.html", revealed = True) 
        
    elif form.password != form.repassword:

        flash("Oops, passwords aren't matching!", 'error-message')
        
        return render_template("auth/gate.html", revealed = True)
        

    return render_template("auth/gate.html", revealed = True)

@auth.route('/reset', methods = ["POST"])
def reset_pwd():
    pass