import math


def area(r):
    '''
    Returns the area of a circle by its radius

        Parameters:
            r (float): circle radius length

        Return value:
            circle_area (float): circle area
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Returns the perimeter of a circle by its radius

        Parameters:
            r (float): circle radius length

        Return value:
            circle_perimeter (float): circle perimeter
    '''
    return 2 * math.pi * abs(r)
