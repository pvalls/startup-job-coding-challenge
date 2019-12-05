from createCity import createCity
import json
from main import init, getSunlightHours

city = createCity()

# convert city into JSON:
city_json = json.dumps(city)

# Initialize city in the main application interface
init(city_json)

# Run some tests...
# Use common sense/visual understanding of the POBLENOU neighborhood
# by looking at the given instructions illustration
print("POBLENOU NEIGHBORHOOD")
print("For building '01' apartment 3, the sunlight hours are: " + getSunlightHours("POBLENOU", "01", 3))
print("For building '30' apartment 0, the sunlight hours are: " + getSunlightHours("POBLENOU", "30", 0))
print("For building 'CEM' apartment 4, the sunlight hours are: " + getSunlightHours("POBLENOU", "CEM", 4))
print("For building '01' apartment 7, the sunlight hours are: " + getSunlightHours("POBLENOU", "Aticco", 7))


# Run some other Exception error tests
# getSunlightHours("GRACIA", "NONEXISTENT", 5)
# getSunlightHours("POBLENOU", "01", 99)