from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class NewUserForm(FlaskForm):
    """Form for creating a new user"""

    username = StringField("Username",
                        validators=[InputRequired()])
    password = StringField("Password",
                        validators=[InputRequired()])
    email = StringField("Email",
                        validators=[InputRequired()])
    first_name = StringField("Username",
                        validators=[InputRequired()])
    last_name = StringField("Username",
                        validators=[InputRequired()])

