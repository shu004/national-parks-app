"""Server for national park app"""

from flask import (Flask, render_template, session, redirect, request, flash)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']

@app.route('/')
def homepage():
    """view national park homepage, user login"""
    parks = crud.get_parks()
    return render_template('homepage.html', parks=parks)

@app.route('/createaccount')
def new_user():
    """new users creating an account"""
    return render_template('new_user.html')

#post request, form points to /users and this is a /users route but viewers do not see
@app.route('/users', methods=["POST"])
def register_user():
    """create a new user"""
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    if crud.get_user_by_email(email):
        flash("You've already created an account, please log in")
    elif crud.get_user_by_username(username):
        flash("This username has been taken, please try another one")
        return redirect('/createaccount')
    else:
        crud.create_user(username, email, password)
        flash('Account created, please log in')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    """logging an existing user"""
    username = request.form.get("username")
    password = request.form.get("password")

    if crud.verify_password(username, password):
        return redirect(f'/profile/{username}')
    else:
        flash('Incorrect Login')
        return redirect('/')

@app.route('/profile/<username>')
def show_user_profile(username):
    """show user profile"""
    user = crud.get_user_by_username(username)
    return render_template('profile_page.html', user=user)

@app.route('/<park_id>')
def show_park(park_id):
    """Show details on each park"""
    park = crud.get_park_by_id(park_id)
    return render_template('park_details.html', park=park)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
