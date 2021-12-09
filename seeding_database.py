"""seeding data into database, only run this file once to create db"""

import os
import crud, server, model
from nps_api import NPS_DATA
import csv
from sqlalchemy import func

os.system('dropdb nps')
os.system('createdb nps')
model.connect_to_db(server.app)
model.db.create_all()

#feeding NPS to database
for park in NPS_DATA:
    name, img, description, latitude, longitude, address, fee, weather, state, hours_exception = (
        park['name'],
        park['image'],
        park['description'],
        park['latitude'],
        park['longitude'],
        park['address'],
        park['fees'],
        park['weather'],
        park['state'],
        park['exception_description']
    )
    crud.create_park(name, img, description, latitude, longitude, address, fee, weather, state, hours_exception)

# creating fake users(for testing)
for n in range(10):
    username =f"user{n}"
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(username, email, password) #generate 10 users

#feeding hiking trails to database
with open ('hiking_trail_data/popular_hikes.csv') as file:
    data = csv.reader(file)
    next(data) #skip first line

    for row in data:
        trail_name=row[0]
        rating=row[12]
        difficulty=row[9]
        park_name=row[1]
        park_id = model.db.session.query(model.Park.park_id).filter(func.lower(model.Park.park_name) == func.lower(park_name))

        crud.create_trail(trail_name, rating, difficulty, park_id)
