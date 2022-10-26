

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Defines User model"""

    __tablename__ = "users"

    username = db.Column(
        db.String(20),
        primary_key=True,
        unique=True
    )

    password = db.Column(
        db.String(100),
        nullable=False,
    )

    email = db.Column(
        # Is there a way to specifically restrict here to email
        db.String(50),
        nullable=False,
        unique=True,
    )

    first_name = db.Column(
        db.String(30),
        nullable=False,
    )

    last_name = db.Column(
        db.String(30),
        nullable=False,
    )

    @classmethod
    # Is cls magic?
    def register(
        cls,
        username,
        password,
        email,
        first_name,
        last_name
    ):
        """Create user w/hashed password and return user."""

        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(
            username=username,
            password=hashed,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

    @classmethod
    def authenticate(
        cls,
        username,
        password
    ):
        """ Checks that user exists and password is correct. """
        #todo: add user return to docstring
        user = User.query.filter_by(username=username).one_or_none()

        if user and bcrypt.check_password_hash(user.password, password):
            return user

        else:
            return False
