"""Flask app for User Authentication"""
#from crypt import methods
from flask import Flask, jsonify, request, render_template, redirect, flash
from forms import CreateUserForm, LoginForm

from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "GET OUTTA MY DB!!!"


@app.get('/')
def redirect_register():
    """ Redirect to register. """

    return redirect('/register')


@app.route('/register', methods=["GET", "POST"])
def register():
    """ Display registration form,
    register/create user with accepted data """

    form = CreateUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.username.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        existing_user = User.query.filter(User.username == username).one_or_none()

        if not existing_user:

            user = User.register(
                username,
                password,
                email,
                first_name,
                last_name,
            )

            db.session.add(user)
            db.session.commit()

            return redirect("/secret")

        else:
            flash("Username already exists!")
            return render_template('create-user.html', form=form)
    else:
        return render_template('create-user.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if User.authenticate(username, password):

            return redirect("/secret")

        else:
            flash("Incorrect username or password.")
            return render_template('login.html', form=form)

    else:
        return render_template('login.html', form=form)



@app.get('/secret')
def show_secret_page():
    return render_template('secrets.html')
