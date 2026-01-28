from flask import Flask, render_template
from db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///migrations.db'


db.init_app(app)

@app.route('/')
def base():
    return render_template('index.html')

@app.post('/login')
def login():
    return render_template('login.html')

@app.post('/crud')
def home():
    return render_template('form.html')

