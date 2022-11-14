'''
Main.py

https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1&api_key=3TqBgy1PDhnZxSnY7FP8Mi9X1XPi4UjXmS85gHz1
'''
import json
import requests

response = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1&api_key=3TqBgy1PDhnZxSnY7FP8Mi9X1XPi4UjXmS85gHz1')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    #print(parsed_json)
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])