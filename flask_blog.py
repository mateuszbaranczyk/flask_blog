from datetime import time
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "strong_secret_key"

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=1, port="5000")
