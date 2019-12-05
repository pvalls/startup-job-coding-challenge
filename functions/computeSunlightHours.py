import math
import time as t


def computeSunlightHours(sunrise_time, sunset_time, sunrise_angle, sunset_angle):
    # The sun is at its highest (we go from sunrise to sunset phase)
    # at the time in between sunrise_time and sunset_time: midday
    sunrise_time_seconds = t.mktime(sunrise_time)
    sunset_time_seconds = t.mktime(sunset_time)
    midday_time_seconds = (sunrise_time_seconds + sunset_time_seconds) / 2
    halfday_duration = midday_time_seconds - sunrise_time_seconds

    # Percentage of morning/afternoon time lost
    morning_lost_time_percentage = sunrise_angle / (math.pi / 2)
    afternoon_lost_time_percentage = sunset_angle / (math.pi / 2)

    # Compute how many seconds of morning/afternoon are lost because of other building shadows
    morning_lost_seconds = halfday_duration * morning_lost_time_percentage
    afternoon_lost_seconds = halfday_duration * afternoon_lost_time_percentage

    # Resulting sunrise and sunset time taking into account shadow angles (lost time)
    result_sunrise_time_seconds = sunrise_time_seconds + morning_lost_seconds
    result_sunset_time_seconds = sunset_time_seconds - afternoon_lost_seconds

    # Convert back frorm seconds to "time_strtuct" object
    result_sunrise_time = t.localtime(result_sunrise_time_seconds)
    result_sunset_time = t.localtime(result_sunset_time_seconds)

    # Convert from "time_strtuct" object to string  in format hh:mm:ss
    final_sunrise_time_str = t.strftime('%H:%M:%S', result_sunrise_time)
    final_sunset__time_str = t.strftime('%H:%M:%S', result_sunset_time)

    return ([final_sunrise_time_str, final_sunset__time_str])
