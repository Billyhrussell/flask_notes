from flask import Flask, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
from forms import RegisterUserForm, LoginUserForm, CSRFProtectForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.get("/")
def root():
    """Redirect to /register"""

    return redirect("/register")

@app.route("/register", methods = ["GET", "POST"])
def add_new_user():
    """Handle new-user form:
    - if form not filled out/invalid: show form
    - if valid: add new user and redirect to /secret"""

    form = RegisterUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, email, first_name, last_name)
        db.session.add(user)
        db.session.commit()

        flash("user created")
        return redirect("/secret")
    else:
        return render_template("register.html", form = form)

@app.route("/login", methods = ["GET", "POST"])
def login():
    """Handle login-user form:
    - if form not filled out/invalid: show form
    - if valid: log user in and redirect to /secret"""

    form = LoginUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session["user_id"] = user.username
            return redirect("/secret")

        else:
            form.username.errors = ["Bad username/password"]

    return render_template("login.html", form=form)

@app.get("/users/<username>")
def show_user_info(username):
    """Hidden page for logged-in users only"""

    user = User.query.get_or_404(username)

    if "user_id" not in session:
        flash("You must be logged in to view!")
        return redirect("/")

    else:
        return render_template("user-information.html", user = user)

@app.post("/logout")
def logout_user():
    """Logs user out and redirects to homepage"""

    form = CSRFProtectForm()

    if form.validate_on_submit():

        session.pop("user_id", None)

    return redirect("/")

