import math

# Converts bearing (0 - 360 degrees) to a vector tuple
def bearing_to_vector(bearing):
    bearing %= 360
    x_multiplier = 1 if bearing <= 180 else -1
    y_multiplier = 1 if bearing <= 90 or bearing >= 270 else -1

    if bearing <= 180 and bearing > 90:
        bearing = 180 - bearing
    elif bearing > 180 and bearing <= 270:
        bearing = bearing - 180
    elif bearing > 270:
        bearing = 360 - bearing

    # Convert back to radians
    bearing = (bearing / 180.0) * math.pi

    return (math.sin(bearing) * x_multiplier, math.cos(bearing) * y_multiplier)
    