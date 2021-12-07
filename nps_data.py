import requests
import os

API_ENDPOINT = "https://developer.nps.gov/api/v1/parks?limit=600"
API_KEY = os.environ['NPS_API_KEY']
parameters = {"api_key": API_KEY}

#getting response back from nps
response = requests.get(url=API_ENDPOINT, params=parameters)
data = response.json()
#465 national parks
unfiltered_nps = data['data']

#63 national parks with the name NATIONAL PARK 
filtered_national_parks = [park for park in unfiltered_nps if "National Park" in park["fullName"]]

national_parks = []

for park in filtered_national_parks:
    park_obj = {}
    park_obj['fullname'] = park['fullName']
    park_obj['location'] = (park['latitude'], park['longitude'])
    park_obj['description'] = park['description']
    park_obj['image'] = park['images'][0]['url']
    national_parks.append(park_obj)

for park in national_parks:
    print("\n")
    print(park['fullname'])
    print("\n")


