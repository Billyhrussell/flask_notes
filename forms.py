from wtforms import StringField, PasswordField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class RegisterUserForm(FlaskForm):
    """Form for creating a new user"""

    username = StringField("Username",
                        validators=[InputRequired()])
    password = PasswordField("Password",
                        validators=[InputRequired()])
    email = EmailField("Email",
                        validators=[InputRequired()])
    first_name = StringField("First Name",
                        validators=[InputRequired()])
    last_name = StringField("Last Name",
                        validators=[InputRequired()])

class LoginUserForm(FlaskForm):
    """Form for logging in user"""

    username = StringField("Username",
                            validators=[InputRequired()])
    password = PasswordField("Password",
                            validators=[InputRequired()])

class CSRFProtectForm(FlaskForm):
    """Form for CSRF Protection"""

