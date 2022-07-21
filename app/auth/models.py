from email.policy import default
from sqlalchemy import nullslast
from app import db
from app.auth.helper import get_student_info, decompose_email

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'users'

    # User Name
    name        = db.Column(db.String(128),  nullable=False)

    # Identification Data: email & password
    email       = db.Column(db.String(128),  nullable=False, unique=True)

    password    = db.Column(db.String(192),  nullable=False)

    # Institution of affiliation
    institution = db.Column(db.String(128), nullable=False)


    # New instance instantiation procedure
    def __init__(self, email, password, name = None):

        self.email    = email
        self.password = password

        # Extract Institution from email address
        self.institution = decompose_email(email).get('institution')

        if not name:
            try:
                more_info = get_student_info(decompose_email(email).get('uni'))
                if more_info:
                    self.name = more_info["name"]
            except:
                self.name = "unspecified"


    def __repr__(self):
        return '<User %r>' % (self.name) 

    def register(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True

        except Exception as e:
            print(e)
            return False