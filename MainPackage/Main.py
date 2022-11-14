'''
Main.py

Name: Jack Hutz and Greysen Webb
email: hutzjm@mail.uc.edu & webbgp@mail.uc.edu
Assignment: Assignment 11 
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This program grabs data available through the FoodData Central API on the USDA website
Citations:
Anything else that's relevant: https://api.nal.usda.gov/fdc/v1/foods/list?api_key=3TqBgy1PDhnZxSnY7FP8Mi9X1XPi4UjXmS85gHz1
'''

import json
import requests

response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=3TqBgy1PDhnZxSnY7FP8Mi9X1XPi4UjXmS85gHz1')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    #print(parsed_json)
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])
 
#print(parsed_json['fdcId']))        # The number of parks that were returned
    
'''
# Get the value associated with paresed_json['data']
for park in parsed_json[1]:
    print(park)
fdcId
description
dataType
publicationDate
foodCode
foodNutrients
'''

# This prints out each type of food description available
print("Descriptions:")

for index in range(len(parsed_json)):
    print(parsed_json[index]['description'])
    

# This for loop sums up the total number of food ID's  
print("")
total = 0     
for index in range(len(parsed_json)):
    parsed_json[index]['fdcId']
    total += 1   
print("There are " + str(total) + " foods in the list")
print("")

# Prints out specific details of Abalone
print("There is " + str(parsed_json[1]['foodNutrients'][0]['amount']) + parsed_json[1]['foodNutrients'][0]['unitName'] + " of " +parsed_json[1]['foodNutrients'][0]['name'] + " in " + parsed_json[1]['description'])
print("There is " + str(parsed_json[1]['foodNutrients'][3]['amount']) + parsed_json[1]['foodNutrients'][3]['unitName'] + " of " +parsed_json[1]['foodNutrients'][3]['name'] + " in " + parsed_json[1]['description'])
        
        
    
    