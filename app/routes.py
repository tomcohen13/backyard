from flask import render_template, url_for, redirect, session, request
from app import app
from app.auth import routes
from app import db
from app.models import *

@app.route("/", methods=["GET", "POST"])
def index():
    if "user_id" in session:
        try:
            uid = session["user_id"]
            user = User.query.filter_by(id=uid).first()
            inst = Institution.query.filter_by(id = user.institution_id).first()
            return redirect(url_for("home", institution_code = inst.store_code))
        except:
            return redirect(url_for("gate"))

    return redirect(url_for("gate"))

@app.route("/<institution_code>/home", methods=["GET", "POST"])
def home(institution_code):

    try:
        uid = session["user_id"]

    except:
        return redirect(url_for("gate"))
    
    user = User.query.filter_by(id = uid).first()
    
    # Load apps
    # apps = db.universities.find_one({"page_code": institution})
    
    return render_template("home.html", institution = institution_code,
                                        name = user.name, 
                                        profile_pic = user.profile_picture)