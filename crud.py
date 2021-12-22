"""CRUD operations"""

from flask.scaffold import F
from model import db, User, Trail, Park, UserTrail, SavedParks, Pictures, connect_to_db

#------------------------User Functions----------------------#
def create_user(username, email, password):
    """create and return a new user"""
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """return a user by email"""
    return User.query.filter(User.email == email).first()

def get_user_by_username(username):
    """return a user by username"""
    return User.query.filter(User.username == username).first()

def get_user_by_id(user_id):
    """return a user by id"""
    return User.query.get(user_id)

def verify_password(username, password):
    """verify if user exist and password"""
    user = User.query.filter(User.username == username).first()
    if user is None:
        return False
    else:
        return user.password == password


#------------------------Park Functions----------------------#
def create_park(name, img, description, latitude, longitude, address, fee, weather, state, hours):
    """create and return a national park"""
    park = Park(park_name=name,
                img=img,
                description=description,
                latitude=latitude,
                longitude=longitude,
                address=address,
                fee=fee,
                weather=weather,
                state=state,
                hours_exception=hours)
    db.session.add(park)
    db.session.commit()

    return park

def get_parks():
    """return all parks"""
    return Park.query.all()

def get_park_by_id(park_id):
    """return park by id"""
    return Park.query.get(park_id)

def get_park_by_name(name):
    """return park by name"""
    return Park.query.filter(Park.park_name == name).first()

def get_location_by_id(park_id):
    """return a tuple of lat and long by park id"""
    lat = db.session.query(Park.latitude).filter(Park.park_id==park_id).first()[0]
    long = db.session.query(Park.longitude).filter(Park.park_id==park_id).first()[0]
    return (lat, long)


#------------------------ Saving Park Functions ---------------------#
def get_saved_park_by_username(username):
    list_of_ids = []
    list_of_tups = db.session.query(SavedParks.park_id).filter(SavedParks.username == username).all()
    for tup in list_of_tups:
        list_of_ids.append(tup[0])
    return list_of_ids


def insert_saved_park(username, park_id):
    """insert into user_saved_parks table"""
    saved_park = SavedParks(username=username, park_id=park_id)
    db.session.add(saved_park)
    db.session.commit()
    return saved_park

def user_saved_park(username, park_id):
    """return true if user already has the park saved in user_saved_parks table"""
    #getting all the entries with that username (a list)
    saved_parks = SavedParks.query.filter(SavedParks.username == username).all()

    for park in saved_parks:
        if int(park_id) == park.park_id:
            return True
    return False

#------------------------Trail Functions----------------------#

def create_trail(name, state, length, elevation_gain, difficulty, route_type, rating, park_id):
    """create and return a trail"""
    trail = Trail(trail_name=name, state=state, length=length, elevation_gain=elevation_gain, difficulty=difficulty, route_type=route_type, rating=rating, park_id=park_id)
    db.session.add(trail)
    db.session.commit()

def get_trails_by_park_id(park_id):
    """return a list of trails by id"""
    trails = db.session.query(Trail).filter(Trail.park_id==park_id).all()
    return trails


#------------------------ User Photos Functions ----------------------#

def insert_photo(username, url):
    """insert uploaded photo url to database"""
    photo = Pictures(username=username, url=url)
    db.session.add(photo)
    db.session.commit()
    return photo


def get_photo_by_username(username):
    """get a list of user uploaded url from pictures table using username"""
    list_urls = []
    list_of_tups = db.session.query(Pictures.url).filter(Pictures.username==username).all()
    for tup in list_of_tups:
        list_urls.append(tup[0])

    return list_urls





if __name__ == '__main__':
    from server import app
    connect_to_db(app)