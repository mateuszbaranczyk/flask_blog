from flask import flash, redirect, render_template, url_for

from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm


posts = [
    {
        "author": "Mat",
        "title": "Dummy post 1",
        "date": "02-01-2021",
        "content": "Dummy content1",
    },
    {
        "author": "Pat",
        "title": "Dummy post 2",
        "date": "03-01-2021",
        "content": "Dummy content2",
    },
]


@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for user {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@dupa.pl" and form.password.data == "password":
            flash(f"Hello!", "success")
            return redirect(url_for("home"))
        else:
            flash(f"Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)
