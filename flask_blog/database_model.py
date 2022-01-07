from datetime import datetime

from flask_blog import database


class User(database.Model):
    pk = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    image_file = database.Column(
        database.String(20), nullable=False, default="default.jpg"
    )
    password = database.Column(database.String(120), nullable=False)
    posts = database.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email}', {self.image_file}')"


class Post(database.Model):
    pk = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), unique=True, nullable=False)
    date_posted = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow
    )
    content = database.Column(database.Text, nullable=False)
    user_pk = database.Column(
        database.Integer, database.ForeignKey("user.pk"), nullable=False
    )

    def __repr__(self):
        return f"User('{self.title}', {self.date_posted}')"
