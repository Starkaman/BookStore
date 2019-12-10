from flask import Flask, render_template, request
from database import *
app = Flask(__name__)

@app.route("/", methods = ["GET", " POST"])
def home():
    if request.form:
        book = Book(title = request.form.get("title"))
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    
    return render_template('index.html', books = books)


