"""Models for User"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt

db = SQLAlchemy()

class User(db.Model):
    """User"""

    __tablename__ = "users"

    username = db.Column(db.String(20),
                        primary_key = True)
    password = db.Column(db.String(100),
                        nullable = False)
    email = db.Column(db.String(50),
                        nullable = False)
    first_name = db.Column(db.String(30),
                        nullable = False)
    last_name = db.Column(db.String(30),
                        nullable = False)

    def register(cls, username, password, email, first_name, last_name):

        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(username = username, password= hashed, email = email,
                     first_name = first_name, last_name = last_name)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
