
def area(a):
    '''
    Returns the area of a square on its side

        Parameters:
            a (float): square side length

        Return value:
            square_area (float): square area
    '''
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("Side of square must be number")
    return a * a


def perimeter(a):
    '''
    Returns the perimeter of the square on its side

        Parameters:
            a (float): square side length

        Return value:
            square_perimeter (float): square perimeter
    '''
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("Side of square must be number")
    return 4 * abs(a)
