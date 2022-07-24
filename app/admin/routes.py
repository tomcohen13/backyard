# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.admin.forms import AddInstitution

# Import data models
from app.models import Institution

from app.routes import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/add_institution", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        
        form = AddInstitution(request.form)
        if form.validate():

            new_inst = Institution(form.name.data, 
                                    form.primary_color.data, 
                                    form.store_code.data, 
                                    form.email_code.data
                                    )

            if not Institution.query.filter_by(name=form.name.data).first():
                new_inst.register()
            else:
                flash("Already registered!", 'error-message')

        flash_errors(form)
        return "Added"
    else:
        try:
            uid = session["uid"]
            user = User.query.filter_by(id = uid).first()
            # if user.role == "0":
            return render_template("admin/add_institution.html")
        except:
            return redirect(url_for("auth.gate"))


def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')