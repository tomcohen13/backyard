# Import Form
from flask_wtf import Form

from wtforms import EmailField, PasswordField, StringField

# Import Form validators
from wtforms.validators import DataRequired, Email, EqualTo, Regexp

# Define the login form (WTForms)

class AddInstitution(Form):

    name    =   StringField('Name', [DataRequired(message='Must provide a name')])

    primary_color   = StringField('Color', [DataRequired(message='Must provide a formatted color')])

    store_code = StringField('Store Code', [DataRequired(message='Must provide a unique code for the institution\'s app store (could be an abbreviation)')])

    email_code = StringField("Email Code", [DataRequired(message='Must provide the email code of the institution (xxxx@<email_code>.edu)')])
