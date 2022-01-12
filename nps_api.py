import requests
import os

NPS_API_ENDPOINT = "https://developer.nps.gov/api/v1/parks?limit=600"
API_KEY = os.environ['NPS_API_KEY']
parameters = {"api_key": API_KEY}

response = requests.get(url=NPS_API_ENDPOINT, params=parameters)
data = response.json()
unfiltered_nps = data['data'] #465 parks

#Filtered data down to 62 parks
filtered_national_parks = [park for park in unfiltered_nps if "National Park" in park["fullName"] and park["fullName"] != 'Wolf Trap National Park for the Performing Arts']


#List of national parks with the relevant data to my db
NPS_DATA = []

for park in filtered_national_parks:
    park_obj = {}
    park_obj['name'] = park['fullName']
    park_obj['image'] = park['images'][0]['url']
    park_obj['description'] = park['description']
    park_obj['fees'] = park['entranceFees'][0]['cost']
    park_obj['weather'] = park['weatherInfo']
    park_obj['state'] = park['states']
    park_obj['address'] = [park['addresses'][0]['line2'], park['addresses'][0]['city'], park['addresses'][0]['stateCode'], park['addresses'][0]['postalCode']]
    park_obj['latitude'] = park['latitude']
    park_obj['longitude'] = park['longitude']
    park_obj['exception_description'] = park['operatingHours'][0]['description']
    NPS_DATA.append(park_obj)






