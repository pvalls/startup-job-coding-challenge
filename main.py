# main.py - Python 3.7.5
# Coding Challenge - Sunlight Hours
# Solution proposal submitted by Pol Valls Rué.

import json
import time as t
from functions.getBuilding import getBuilding
from functions.getNeighborhood import getNeighborhood
from functions.apartmentExists import apartmentExists
from functions.computeAngleTrigonometry import computeAngleTrigonometry
from functions.computeSunlightHours import computeSunlightHours

# Define the sunrise/sunset time to work with. Use format 'hh:mm:ss'
sunrise_time_str = '08:14:00'
sunset_time_str = '17:25:00'

# Convert to "struct_time" object
sunrise_time = t.strptime(sunrise_time_str, '%H:%M:%S')
sunset_time = t.strptime(sunset_time_str, '%H:%M:%S')

# Initialize city as a global list variable
city = list()


# API FUNCTIONS #
# init​ method that takes a String containing a JSON describing the city
def init(city_json):
    global city
    city = json.loads(city_json)


# getSunlightHours. It returns the sunlight hours as a string like “hh:mm:ss - hh:mm:ss” in 24hr format.
def getSunlightHours(neighborhood_name, building_name, apartment_number):

    # Try to extract the indicated neighborhood and indicated building object from city
    try:
        neighborhood = getNeighborhood(city, neighborhood_name)
        building = getBuilding(neighborhood, building_name)
    except:
        raise Exception("Error: The given neighborhood or building does not exist in the current city.")

    # Check if the apartment exists
    apartmentExists(building, apartment_number)

    # Place the indicated apartment in a 2D coordinate system.
    x = building.get("distance")
    y = apartment_number*neighborhood.get("apartments_height")

    # Compute the greatest angle during sunrise/sunset at which there is a higher apartment blocking sunlight
    [sunrise_angle, sunset_angle] = computeAngleTrigonometry(neighborhood, building_name, x, y)

    # Using the default sunrise and sunset time as well as the shadow angles found, compute resulting sunlight hours
    [final_sunrise_time_str, final_sunset__time_str] = computeSunlightHours(sunrise_time, sunset_time, sunrise_angle, sunset_angle)

    # print(final_sunrise_time_str + " - " + final_sunset__time_str)
    return (final_sunrise_time_str + " - " + final_sunset__time_str)
