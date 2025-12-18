def area(a, b):
    '''
    Returns the area of the rectangle on its sides

        Parameters:
            a (float): rectangle height length
            b (float): rectangle width length

        Return value:
            rectangle_area (float): rectangle area
    '''
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
    return (abs(a) + abs(b)) * 2