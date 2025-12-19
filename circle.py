import math


def area(r):
    '''
    Returns the area of a circle by its radius

        Parameters:
            r (float): circle radius length

        Return value:
            circle_area (float): circle area
    '''
    if (not isinstance(r, int) and not isinstance(r, float)):
        raise TypeError("Radius of circle must be number")
    return math.pi * r * r


def perimeter(r):
    '''
    Returns the perimeter of a circle by its radius

        Parameters:
            r (float): circle radius length

        Return value:
            circle_perimeter (float): circle perimeter
    '''
    if (not isinstance(r, int) and not isinstance(r, float)):
        raise TypeError("Radius of circle must be number")
    return 2 * math.pi * abs(r)
