"""CRUD operations"""

from model import db, User, Trail, Park, UserTrail, UserParks, connect_to_db


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
    user = User.query.filter(User.username == username).first()
    if user is None:
        return False
    else:
        return user.password == password


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


def create_trail(name, rating, difficulty, park_id):
    """create and return a trail"""
    trail = Trail(trail_name=name, rating=rating, difficulty=difficulty, park_id=park_id)
    db.session.add(trail)
    db.session.commit()

def get_trails_by_park_id(park_id):
    """return a list of trails by id"""
    trails = db.session.query(Trail).filter(Trail.park_id==park_id).all()
    return trails









if __name__ == '__main__':
    from server import app
    connect_to_db(app)