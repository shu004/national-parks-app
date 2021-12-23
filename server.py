"""Server for national park app"""

from flask import (Flask, render_template, session, redirect, request, flash, jsonify, url_for)
from model import SavedParks, connect_to_db
import crud
from jinja2 import StrictUndefined
import os
import cloudinary.uploader
import requests
from datetime import datetime


from nps_api import API_KEY


app = Flask(__name__)
app.secret_key = os.environ['secret_key']

CLOUDINARY_KEY = os.environ['CLOUDINARY_API_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_API_SECRET']
CLOUD_NAME = "dumwtiism"


@app.route('/')
def homepage():
    """view national park homepage and user login"""
    return render_template('homepage.html')


@app.route('/createaccount')
def new_user():
    """new users creating an account"""
    return render_template('registration.html')


#post request, form points to /users and this is a /users route but viewers do not see
@app.route('/users', methods=["POST"])
def register_user():
    """create a new user"""
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    if crud.get_user_by_email(email):
        flash("You've already created an account, please log in")
    elif crud.get_user_by_username(username):
        flash("This username has been taken, please try another one")
        return redirect('/createaccount')
    else:
        crud.create_user(name, username, email, password)
        flash('Account created, please log in')
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    """logging an existing user"""
    username = request.form.get("username")
    password = request.form.get("password")

    if crud.verify_password(username, password):
        session['username'] = username
        return redirect(f'/')
    else:
        flash('Incorrect Login')
        return redirect('/')


@app.route('/logout')
def logout():
    """logging out a user/session"""
    session.clear()
    return redirect('/')


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
    #the park_id is the paramter we are passing in the queryString
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
    #if there isn't a session, user not logged on. without this, it will throw an error
    #when reading user_has_saved_park
    if not session:
        return render_template('park_details.html', park=park, trails=trails)
    else:
        user_has_saved_park = crud.user_saved_park(session['username'], park_id)
        return render_template('park_details.html', park=park, trails=trails, user_has_saved_park=user_has_saved_park)



@app.route('/add-badge', methods=['POST'])
def add_badge():
    """adding saved park to our database"""
    username = request.json.get('username')
    park_id = request.json.get('parkId')
    crud.insert_saved_park(username, park_id)
    return {"success": True, "status": "You've added this badge to your profile!"}



@app.route('/profile/<username>')
def show_user_profile(username):
    """show user profile"""
    user = crud.get_user_by_username(username)
    saved_park_id = crud.get_saved_park_by_username(username)
    entries = crud.get_entry_by_username(username)
    return render_template('profile_page.html', user=user, saved_park_id=saved_park_id, entries=entries)



@app.route('/profile/<username>/post-form-data', methods=['POST'])
def post_form(username):
    """post the picture from form to database"""
    my_file = request.files['my-file']

    result = cloudinary.uploader.upload(my_file,
                                        api_key=CLOUDINARY_KEY,
                                        api_secret=CLOUDINARY_SECRET,
                                        cloud_name= CLOUD_NAME)

    url = result['secure_url']
    text = request.form.get("blog-text")
    now = datetime.now()
    month = now.strftime("%b")
    day = now.strftime("%e")
    year = now.strftime("%Y")
    date = f"{month} {day}, {year}"

    crud.insert_entry(username, url, text, date)
    return redirect (f"/profile/{username}")














if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
