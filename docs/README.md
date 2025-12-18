
# Geometric lib

The library provides functions for calculating the characteristics of geometric shapes based on their parameters.

## Circle

### area(r)

Returns the area of a circle by its radius

Parameters:
r (float): circle radius length

Return value:
circle_area (float): circle area

Formula:
$S = \pi * r ^ 2$

Usage example:

``` Python
print(circle.area(10))
print(circle.area(0))
print(circle.area(2))
```

Output:

``` Python
314.1592653589793
0.0
12.566370614359172
```

### perimeter(r)

Returns the perimeter of a circle by its radius

Parameters:
r (float): circle radius length

Return value:
circle_perimeter (float): circle perimeter

Formula:
$P = 2 * \pi * r$

Usage examples:

``` Python
print(circle.perimeter(10))
print(circle.perimeter(0))
print(circle.perimeter(2))
```

Output:

``` Python
62.83185307179586
0.0
12.566370614359172
```

## Rectangle

### area(a, b)

Returns the area of the rectangle on its sides

Parameters:
a (float): rectangle height
b (float): rectangle width

Return value:
rectangle_area (float): rectangle area

Formula:
$ S = a * b $

Usage examples:

``` Python
print(rectangle.area(10, 3))
print(rectangle.area(0, 2.4))
print(rectangle.area(1.2, 7.3))
```

Output:

``` Python
30
0.0
8.76
```

### perimeter(a, b)

Returns the perimeter of the rectangle along its sides

Parameters:
a (float): rectangle height length
b (float): rectangle width length

Return value:
rectangle_perimeter (float): rectangle perimeter

Formula:
$P = 2 *(a + b)$

Usage examples:

``` Python
print(rectangle.perimeter(10, 3))
print(rectangle.perimeter(0, 2.4))
print(rectangle.perimeter(1.2, 7.3))
```

Output:

``` Python
26
4.8
17.0
```

## Square

### area(a)

Returns the area of a square on its side

Parameters:
a (float): square side length

Return value:
square_area (float): square area

Formula:
$S = a ^ 2$

Usage examples:

``` Python
print(square.area(7))
print(square.area(0))
print(square.area(3.63))
```

Output:

``` Python
49
0
13.1769
```

### perimeter(a)

Returns the perimeter of the square on its side

Parameters:
a (float): square side length

Return value:
square_perimeter (float): square perimeter

Formula:
$P = a * 4$

Usage examples:

``` Python
print(square.perimeter(7))
print(square.perimeter(0))
print(square.perimeter(3.63))
```

Output:

``` Python
28
0
14.52
```

## Triangle

### area(a, h)

Returns the area of the triangle by its side and height to it

Parameters:
a (float): the length of a triangle side
h (float): height of the triangle to the side with length a

Return value:
triangle_area (float): triangle area

Formula:
$S = \frac{1}{2} * a * h$

Usage examples:

``` Python
print(triangle.area(1, 2))
print(triangle.area(0, 0))
print(triangle.area(4.05, 3.25))
```

Output:

``` Python
1.0
0.0
6.58125
```

### perimeter(a, b, c)

Returns the perimeter of the triangle along its sides

Parameters:
a (float): the length of 1st side of triangle
B (float): the length of 2nd side of triangle
C (float): the length of 3rd side of triangle

Return value:
triangle_perimeter (float): triangle perimeter

Formula:
$P = a + b + c$

Usage examples:

``` Python
print(triangle.perimeter(2, 4, 3))
print(triangle.perimeter(3.25, 9, 6.8))
print(triangle.perimeter(4, 7, 3.48))
```

Output:

``` Python
9
19.05
14.48
```

## Changelog

commit 7111def4fdc14392ac64032866ccd4a37bd1cb88
Add tests

commit f5fa9399dbcbfaecc2c0f4bcc7f5096844dd2d01
Fix negative values processing

commit e924b64f604bb43371287d30a406261f2d303188
Add docs

commit e1744f9cbee576c0eb83183aee597cdc68a660df
Fix bug in rectangle perimeter calculation

commit 0f712fc8326b20ff353b72fc529288f961a022e8
Add new file rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
L-03: Circle and square added
