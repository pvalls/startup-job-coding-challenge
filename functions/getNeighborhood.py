def getNeighborhood(city, neighborhood_name):
    neighborhood_names = [neighborhood_dictionary['neighborhood'] for neighborhood_dictionary in city]
    neighborhood_index = neighborhood_names.index(neighborhood_name)
    return city[neighborhood_index]