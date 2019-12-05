def apartmentExists(building, apartment_number):
    if not(building.get("apartments_count") >= apartment_number + 1 and apartment_number >= 0):
        raise Exception("Error: The given apartment number does not exist in the specified building '" + building.get("name") + "'")
