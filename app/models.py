from uuid import uuid4

from sqlalchemy import ForeignKey
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.String(64), primary_key=True, nullable = False)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'users'

    # User Name
    name        = db.Column(db.String(128), nullable = False)

    # Identification Data: email & password
    email       = db.Column(db.String(128), nullable=False, unique=True, primary_key = True)

    password    = db.Column(db.String(192), nullable=False)

    institution_id = db.Column(db.String(64), db.ForeignKey('institutions.id'), nullable=False)

    is_verified    = db.Column(db.Boolean(), nullable=False)

    profile_picture = db.Column(db.String(128))


    # New instance instantiation procedure
    def __init__(self, email, password, name, institution_id, is_verified = False, profile_picture = ""):

        self.id         = str(uuid4())
        self.email      = email
        self.name       = name
        self.password   = password
        self.is_verified    = is_verified
        self.institution_id = institution_id
            


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

# Helper table
appstores = db.Table('appstores',
    db.Column('app_id', db.String(64), db.ForeignKey('apps.id'), primary_key=True),
    db.Column('institution_id', db.String(64), db.ForeignKey('institutions.id'), primary_key=True)
)


# Institution

class Institution(Base):

    __tablename__ = 'institutions'

    name            = db.Column(db.String(128),  nullable = False, unique = True)
    primary_color   = db.Column(db.String(64), nullable = False)
    # nicknames       = db.Column(db.Array(db.String(64))) # add later
    store_code       = db.Column(db.String(10), unique = True, nullable = False)
    email_code      = db.Column(db.String(32), unique = True, nullable = False)
    # Relationships
    users       = db.relationship('User', backref='user', lazy=True)

    appstore = db.relationship('App', 
                                secondary = appstores, 
                                lazy = "subquery",
                                backref = db.backref('institutions', lazy = True))

    def __init__(self, name, primary_color, store_code, email_code) -> None:
        self.name = name
        self.id = str(uuid4())
        self.primary_color = primary_color
        # self.nicknames = nicknames
        self.store_code = store_code
        self.email_code = email_code

    def register(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True

        except Exception as e:
            print(e)
            return False

class App(Base):

    __tablename__   = 'apps'

    name            = db.Column(db.String(64), unique = True, nullable = False)     
    primary_link    = db.Column(db.String(128), unique = True, nullable = False)
    short_desc      = db.Column(db.String(250), nullable = False)
    long_desc       = db.Column(db.String(500), nullable = False)
    is_locked       = db.Column(db.Boolean, nullable = False)

    def __init__(self, name, link, short, long, locked = False) -> None:
        self.id = uuid4()
        self.name = name
        self.primary_link = link
        self.short_desc = short
        self.long_desc = long
        self.locked = locked

