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
        """Generate hashed password for user, return instance of User"""
        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(username = username, password= hashed, email = email,
                     first_name = first_name, last_name = last_name)

    def authenticate(cls, username, password):
        """Validate that user exists and password is correct
        return user if valid"""
        u = cls.query.filter_by(username = username).one_or_none()

        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return False


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
