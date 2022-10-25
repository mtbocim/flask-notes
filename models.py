

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Defines User model"""

    __tablename__ = "users"

    username = db.Column(
        db.Text(20),
        primary_key=True,
        unique=True
    )

    password = db.Column(
        db.Text(100),
        nullable=False,
    )

    email = db.Column(
        #Is there a way to specifically restrict here to email
        db.Text(50),
        nullable=False,
        unique = True,
    )

    first_name = db.Column(
        db.Text(30),
        nullable=False,
    )

    last_name = db.Column(
        db.Text(30),
        nullable=False,
    )
