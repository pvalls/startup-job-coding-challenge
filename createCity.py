# CREATE TESTING OBJECT / CITY


def createCity():
    # City object is a list of neighborhoods dictionaries
    city = [
        # 1st neighborhood dictionary
        {
            "neighborhood": "POBLENOU",
            "apartments_height": 1.0,
            "buildings": [
                # Builings is a list of building dictionaries
                {
                    "name": "Aticco",
                    "apartments_count": 8.0,
                    "distance": 0.0,
                },

                {
                    "name": "01",
                    "apartments_count": 4.0,
                    "distance": 2.0,
                },

                {
                    "name": "CEM",
                    "apartments_count": 7.0,
                    "distance": 5.0,
                },

                {
                    "name": "30",
                    "apartments_count": 1.0,
                    "distance": 8.0,
                },
            ],
        },

        # 2nd neighborhood
        # ...
    ]  # end of city list.

    return city
