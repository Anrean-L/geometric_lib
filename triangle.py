def area(a, h):
    '''
    Returns the area of the triangle by its side and height to it

        Parameters:
            a (float): the length of a triangle side
            h (float): height of the triangle to the side with length a

        Return value:
            triangle_area (float): triangle area
    '''
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
    return abs(a) + abs(b) + abs(c)
