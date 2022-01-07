from enum import unique
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask.scaffold import F
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "strong_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

database = SQLAlchemy(app)


class User(database.Model):
    pk = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    image_file = database.Column(database.String(20), nullable=False, default="default.jpg")
    password = database.Column(database.String(120), nullable=False)
    posts = database.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email}', {self.image_file}')"

class Post(database.Model):
    pk = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), unique=True, nullable=False)
    date_posted = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    content = database.Column(database.Text, nullable=False)
    user_pk = database.Column(database.Integer, database.ForeignKey("user.pk"), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', {self.date_posted}')"
        
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

if __name__ == "__main__":
    app.run(debug=1, port="5000")
