from flask import render_template, url_for, redirect, session, request
from app import app
from app.auth import routes
from app import db

@app.route("/", methods=["GET", "POST"])
def index():
    """
    if "uid" in session:
        try:
            uid = session["uid"]
            user = User.query.filter_by(email=form.email.data).first()
            return redirect(url_for("home", institution = user["institution"]["page_code"]))
        except:
            return redirect(url_for("gate"))

    return redirect(url_for("gate"))
    """
    
    return render_template("homepage.html")

@app.route("/<school_code>/", methods=["GET", "POST"])
def inst_page(school_code):
    # institution = Institution.query.filter_by(page_code = inst_code)
    # return render_template("homepage.html", institution=institution)
    pass