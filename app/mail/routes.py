# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Import the database object from the main app module
from app import db, mail

# Import data models
from app.models import Institution, User

from app.routes_old import *

# Define the blueprint: 'mail', set its url prefix: [APP_URL]/mail
mail = Blueprint('mail', __name__, url_prefix='/mail')

from app.mail import s
from itsdangerous import SignatureExpired, BadSignature

@mail.route("/confirm", methods = ["GET"])
def confirm():
    try: 
        token = request.args.get('token')
        uid = s.loads(token, salt=app.config['MAIL_SALT'], max_age=300000)
        print(uid)
        user = User.query.filter_by(id = uid).first()
        user.is_verified = True
        db.session.commit()

        flash("Yay! You can log in now!", category='success-message')

        return redirect(url_for('auth.gate'))
    
    except SignatureExpired:
        return '<h2>The token is invalid or has expired</h2>'
    except BadSignature:
        return "<h1>Nah</h1>"
    except Exception as e:
        return f"<h1>some other problem: {e}</h1>"
                
            


