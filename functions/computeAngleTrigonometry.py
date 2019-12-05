import math

def computeAngleTrigonometry(neighborhood, building_name, x, y):

    # We assume that the sun goes from 0[rad] to pi/2[rad] (from 0 to 90 degrees for each quadrant).

    # Initialize  sunrise and sunset angles to 0
    sunrise_angle = 0
    sunset_angle = 0

    # Boolean variable to know which angle to compute (sunrise or sunset)
    iterating_eastern_buildings = True

    # iteration of all buildings
    for building in neighborhood.get("buildings"):

        if building.get("name") != building_name:

            # we compute the coordinates x0 and y0 corresponding to
            # the distance and the maximum height of the tallest apartment of each building
            x0 = building.get("distance")
            y0 = building.get("apartments_count") * neighborhood.get("apartments_height")

            # if our given apartment lowest height (y) is higher or equally high than
            # the current building highest apartment height (y0), we can determine
            # that this building will never produce shade to our apartment and continue to next building
            if y >= y0:
                continue

            # With the two apartment points [(x, y), (x0, y0)]
            # compute the angle defined between the line connecting the points and the x-axis
            # (i.e the angle at which sun rays can reach our apartment)
            # (i.e the drawn line is the hypotenuse between delta_x and delta_y)
            delta_x = abs(x - x0)
            delta_y = abs(y0 - y)

            # if we are iterating over the buildings east from our apartment, we compute the sunrise_angle
            if iterating_eastern_buildings:

                # During sunrise,if the calculated sunrise_angle is greater than the current sunrise_angle, update it
                sunrise_angle = max(sunrise_angle, math.atan(float(delta_y / delta_x)))

            # if we are iterating over the buildings west from our apartment
            elif not iterating_eastern_buildings:
                sunset_angle = max(sunset_angle, math.atan(float(delta_y / delta_x)))

        # if our apartment building and the current building are the same,
        # we have iterated over all the easter buildings.
        elif building.get("name") == building_name:
            iterating_eastern_buildings = False

    return [sunrise_angle, sunset_angle]