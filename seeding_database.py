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


#feeding hiking trails to database
with open ('hiking_trail_data/popular_hikes.csv') as file:
    data = csv.reader(file)
    next(data) #skip first line

    for row in data:
        trail_name=row[0]
        park_name=row[1]
        state = row[3]
        length = row[7]
        elevation_gain = row[8]
        difficulty=row[9]
        route_type=row[10]
        rating=row[12]
        #func.lower to lower case both park name in park table and park name in the data sheet to link park ID
        park_id = model.db.session.query(model.Park.park_id).filter(func.lower(model.Park.park_name) == func.lower(park_name))

        crud.create_trail(trail_name, state, length, elevation_gain, difficulty, route_type, rating, park_id)
