import os

from flask import Flask, request, render_template

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir,"bookstore.com"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

class Book(db.Model):
    title = db.Column(db.String(80), unique = True, nullable = False, primary_key =True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

    