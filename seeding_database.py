"""seeding data into database, only run this file once to create db"""

import os
import crud, server, model
from nps_api import NPS_DATA
import csv

os.system('dropdb nps')
os.system('createdb nps')
model.connect_to_db(server.app)
model.db.create_all()


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

with open ('hiking_trail_data/popular_hikes.csv') as file:
    data = csv.reader(file)
    next(data)
    next(data)
    for row in data:
        trail_name=row[0]
        rating=row[12]
        difficulty=row[9]
        trail_id=
        crud.create_trail(trail_name, rating, difficulty)
        

#query national park database for the park.park_name == trail.park_name (or row-10)
