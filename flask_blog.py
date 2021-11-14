from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=1, port="5000")
