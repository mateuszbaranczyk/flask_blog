from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "strong_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
database = SQLAlchemy(app)

from flask_blog import routes
