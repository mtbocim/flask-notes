"""Flask app for User Authentication"""
from crypt import methods
from flask import Flask, jsonify, request, render_template, redirect
from forms import CreateUserForm

from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
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

        return redirect("/secret")

    else:
        return render_template('create-user.html', form=form)