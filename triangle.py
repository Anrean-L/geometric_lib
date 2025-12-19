def area(a, h):
    '''
    Returns the area of the triangle by its side and height to it

        Parameters:
            a (float): the length of a triangle side
            h (float): height of the triangle to the side with length a

        Return value:
            triangle_area (float): triangle area
    '''
    if (not isinstance(a, int) and not isinstance(a, float) or \
        not isinstance(h, int) and not isinstance(h, float)):
        raise TypeError("Side and height of triangle must be numbers")
    return abs(a * h / 2)

def perimeter(a, b, c):
    '''
    Returns the perimeter of the triangle along its sides

        Parameters:
            a (float): the length of 1st side of triangle
            B (float): the length of 2nd side of triangle
            C (float): the length of 3rd side of triangle

        Return value:
            triangle_perimeter (float): triangle perimeter
    '''
    if (not isinstance(a, int) and not isinstance(a, float) or \
        not isinstance(b, int) and not isinstance(b, float) or \
        not isinstance(c, int) and not isinstance(c, float)):
        raise TypeError("Sides of triangle must be numbers")
    return abs(a) + abs(b) + abs(c)
