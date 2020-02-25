# Mohamed Bensaleh
# mob127
# 11254030
# CMPT 141-02

def spaceTime(D):
    """
    Recursive function that calculates the time needed for Zeno's ship to travel a given distance.
    :param D: a floating point number that is a distance in meters
    :return: The time required to travel the given distance
    """
    if D <= 1:
        return 1
    else:
        return (1 + spaceTime(D/2))

distance = float(input("Enter a distance in meters: "))
print(spaceTime(distance), "minutes to travel", distance, "meters")
