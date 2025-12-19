def area(a, b):
    '''
    Returns the area of the rectangle on its sides

        Parameters:
            a (float): rectangle height length
            b (float): rectangle width length

        Return value:
            rectangle_area (float): rectangle area
    '''
    if (not isinstance(a, int) and not isinstance(a, float) or \
        not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("Sides of rectangle must be numbers")
    return abs(a * b)

def perimeter(a, b):
    '''
    Returns the perimeter of the rectangle along its sides

        Parameters:
            a (float): rectangle height length
            b (float): rectangle width length

        Return value:
            rectangle_perimeter (float): rectangle perimeter
    '''
    if (not isinstance(a, int) and not isinstance(a, float) or \
        not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("Sides of rectangle must be numbers")
    return (abs(a) + abs(b)) * 2