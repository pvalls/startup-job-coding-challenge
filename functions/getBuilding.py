def getBuilding(neighborhood, building_name):
    buildings_list = neighborhood.get("buildings")
    building_names = [building_dictionary['name'] for building_dictionary in buildings_list]
    building_index = building_names.index(building_name)
    return buildings_list[building_index]