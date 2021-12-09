"""Models for national park app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(18), nullable=False)

    #many user to many trails
    trails = db.relationship('Trail', secondary='user_saved_trails', back_populates='users')

    #many users to many parks
    pictures = db.relationship('UserParks', back_populates='user')

    def __repr__(self):
        return f"<User user_id={self.user_id}, username={self.username}, email={self.email}>"


class Trail(db.Model):
    """A trail."""

    __tablename__= "trails"

    trail_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trail_name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    difficulty = db.Column(db.Integer, nullable=True)
    park_id = db.Column(db.Integer, db.ForeignKey("parks.park_id"))

    #one park to many trails
    park = db.relationship('Park', back_populates='trails')

    #many user to many trails
    users = db.relationship('User', secondary='user_saved_trails', back_populates='trails')

    def __repr__(self):
        return f"<Trail trail_id={self.trail_id}, trail_name={self.trail_name}>"



class Park(db.Model):
    """A park."""

    __tablename__= "parks"

    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    park_name = db.Column(db.String, unique=True, nullable=False)
    img = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    address = db.Column(db.String, nullable=True)
    fee = db.Column(db.Float, nullable=True)
    weather = db.Column(db.Text, nullable=True)
    state = db.Column(db.String, nullable=True)
    hours_exception = db.Column(db.Text, nullable=True)

    #one park with many trails
    trails = db.relationship('Trail', back_populates='park')

    #many users to many parks
    pictures = db.relationship('UserParks', back_populates='park')

    def __repr__(self):
        return f"<Park park_id={self.park_id}, park_name={self.park_name}>"


#----------------------------- association tables ------------------------------#
class UserTrail(db.Model):
    """User trail association - user saving a trail"""

    __tablename__="user_saved_trails"

    saved_trails_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    trail_id = db.Column(db.Integer, db.ForeignKey("trails.trail_id"))

    def __repr__(self):
        return f"<Saved Trails user_id={self.user_id}, trail_id={self.trail_id}>"


class UserParks(db.Model):
    """User saving a park and upload pictures"""

    __tablename__="user_saved_parks"

    saved_park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey("parks.park_id"), nullable=False)
    user_picture = db.Column(db.String, nullable=True)

    user = db.relationship("User", back_populates="pictures")
    park = db.relationship("Park", back_populates="pictures")


    def __repr__(self):
        return f"<Saved Parks user_id={self.user_id}, park_id={self.park_id}>"




def connect_to_db(flask_app, db_uri="postgresql:///nps", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)