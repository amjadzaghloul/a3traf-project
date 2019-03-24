from flask import (Flask ,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   flash,
                   jsonify,
                   )
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Post

engine = create_engine('sqlite:///a3traf.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home/contact')
def contact():
    return render_template('contact.html')

@app.route('/home/about')
def about():
    return render_template('about.html')

@app.route('/home/login')
def login():
    return render_template('login.html')

@app.route('/home/register')
def register():
    return render_template('‏register.html')

@app.route('/messages')
def messages():
    messages = session.query(Post).all()
    return render_template('messages.html', messages=messages)

@app.route('/manage')
def manage():
    return render_template('manage.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0' , port = 5000)