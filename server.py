"""Server for national park app"""

from flask import (Flask, render_template, session, redirect, request, flash, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']


@app.route('/')
def homepage():
    """view national park homepage and user login"""
    return render_template('homepage.html')


@app.route('/createaccount')
def new_user():
    """new users creating an account"""
    return render_template('register.html')


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
        session['username'] = username
        return redirect(f'/profile/{username}')
    else:
        flash('Incorrect Login')
        return redirect('/')


@app.route('/logout')
def logout():
    """logging out a user/session"""
    session.clear()
    return redirect('/')


@app.route('/profile/<username>')
def show_user_profile(username):
    """show user profile"""
    user = crud.get_user_by_username(username)
    return render_template('profile_page.html', user=user)


@app.route('/parks.json')
def all_parks():
    """return a dict of all parks"""
    result = crud.get_parks()
    all_parks_dict = {"parks":[]}
    for park in result:
        park = park.to_dict()
        all_parks_dict['parks'].append(park)
    return jsonify(all_parks_dict)


#new route because we are setting up a new queryString to pass back to db
@app.route('/getcoords.json')
def get_park_location():
    park_id = request.args.get("park_id")
    result = crud.get_location_by_id(park_id)
    location_dict = {"lat": result[0], "lng": result[1]}
    return jsonify(location_dict)



@app.route('/search')
def search():
    """redirects to the national park page with search"""
    park_name = request.args.get('parksearch')
    result = crud.get_park_by_name(park_name)
    park_id = result.park_id
    return redirect(f'/park/{park_id}')


@app.route('/park/<park_id>')
def show_park_detail(park_id):
    """Show details on each park"""

    park = crud.get_park_by_id(park_id)
    trails = crud.get_trails_by_park_id(park_id)
    return render_template('park_details.html', park=park, trails=trails)



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
