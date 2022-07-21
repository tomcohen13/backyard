# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.auth.forms import LoginForm, SignupForm

# Import data models
from app.auth.models import User

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

            flash('Welcome %s' % user.name)

            return redirect(url_for('home'))

        flash('Mmmm not the password I got..!', 'error-message')
    
    flash("Can't seem to read that email...", 'error-message')

    return render_template("auth/gate.html", revealed = True)

@auth.route('/signup', methods = ["POST"])
def signup():
    
    form = SignupForm(request.form)
    print(form.data)
    if form.validate():
        
        ### Add another check: if the user is in the db but is unverified, allow to sign up. 
        if User.query.filter_by(email=form.email.data).first():

            flash("You're already registered!", 'error-message')
            
            return render_template("auth/gate.html", revealed = True)

        
        new_user = User(form.email.data, generate_password_hash(form.password.data))

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