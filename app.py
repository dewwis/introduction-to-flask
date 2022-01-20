from datetime import datetime

from flask import Flask,render_template,request,redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite = ///db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    pass

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html', methods=['POST', 'GET'])

@app.route("/profile")
def profile():
    return render_template('profile.html')

hello ="dennis"

"""@app.route('/profile')
def profile():
    return render_template('profile.html')
"""
if __name__ == "__main__":
    app.run (debug=True)