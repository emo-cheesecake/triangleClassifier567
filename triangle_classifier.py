# Tamara Gonzalez Ibarra
# SSW 567 - Spring 2026

import math


def classify_triangle(length1, length2, length3):

    """This function returns a string that classifies whether a triangle 
    is scalene, isosceles, equilateral or a right triangle."""
    # Checks for the validity of the triangle and inputs,
    # as they must be greater than 0 and create a valid triangle.
    if length1 <= 0 or length2 <= 0 or length3 <= 0:
        return "Invalid Triangle"
    if not (length1 + length2 > length3 and
            length1 + length3 > length2 and
            length2 + length3 > length1):
        return "Invalid Triangle"
    # Sorts the sides to identify the largest side (potential hypotenuse)
    sides = sorted([length1, length2, length3])
    a, b, c = sides[0], sides[1], sides[2]
    # Uses Pythagorean theorem to determine if the triangle
    # is a right triangle, variable rightTriangleCheck is a boolean.
    right_triangle_check = math.isclose(a**2 + b**2, c**2)
    # Classifies the triangle based on sides
    if length1 == length2 == length3:
        triangle_type = "Equilateral"
    elif length1 == length2 or length2 == length3 or length1 == length3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    # returns type of triangle
    if right_triangle_check is True:
        return f"{triangle_type} Right Triangle"
    else:
        return f"{triangle_type} Triangle"
    