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
            return redirect(url_for("appstore", institution_code = inst.store_code))
        except:
            return redirect(url_for("auth.gate"))

    return redirect(url_for("auth.gate"))

@app.route("/<institution_code>/home", methods=["GET", "POST"])
def appstore(institution_code):

    try:
        uid = session["user_id"]
        user = User.query.filter_by(id = uid).first()

    except:
        return redirect(url_for("auth.gate"))
    
    inst = Institution.query.filter_by(store_code = institution_code).first()
    # Load apps
    # apps = db.universities.find_one({"page_code": institution})
    print(inst.primary_color)
    
    return render_template("home.html", institution = institution_code,
                                        primary_color = inst.primary_color,
                                        name = user.name, 
                                        profile_pic = user.profile_picture)

@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")