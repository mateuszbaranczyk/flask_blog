from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Mat",
        "title": "Dummy post 1",
        "date": "01.01.2021",
        "content": "Dummy content"
    },
    {
        "author": "Mat",
        "title": "Dummy post 2",
        "date": "01.01.2021",
        "content": "Dummy content"
    },
]

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=1, port="5000")
