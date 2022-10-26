"""Flask app for User Authentication"""
#from crypt import methods
from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    session,
)
from forms import (
    CreateUserForm,
    LoginForm,
    CSRFProtectForm
)

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
    """ 
        Display registration form, register/create user with accepted data.
    """

    form = CreateUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.username.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        existing_user = User.query.filter(
            User.username == username).one_or_none()

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

            session["user_id"] = user.username

            return redirect(f"/user/{username}")

        else:
            flash("Username already exists!")
            return render_template('create-user.html', form=form)
    else:
        return render_template('create-user.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """
        Authenticates user then logs them in and redirects to secrets, 
        or inform of incorrect login information.    
    """

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)

        if user:
            session["user_id"] = user.username
            return redirect(f"/user/{username}")

        else:
            flash("Incorrect username or password.")
            return render_template('login.html', form=form)

    else:
        return render_template('login.html', form=form)


@app.get('/user/<username>')
def show_secret_page(username):
    """
        Shhhh, it's a secret to everyone...

        Shows user info or redirects to login page. 

    """
    
    #we didn't use username right now, but could throw message is
    #username doesn't match session user_id
    #i.e. 401
    if "user_id" not in session:
        form = LoginForm()
        flash("You must be logged in!!!! >:( ")
        return render_template('login.html', form=form)

    else:
        
        user = User.query.get(session["user_id"])
        form = CSRFProtectForm()
        
        return render_template(
            'secrets.html',
            user=user,
            form=form
        )

@app.post('/logout')
def logout_user():
    """Logs out user"""

    form = CSRFProtectForm()
    #it just happens... shh.....
    if form.validate_on_submit():
        session.pop("user_id", None)
    #todo:unauthorized
    return redirect('/')