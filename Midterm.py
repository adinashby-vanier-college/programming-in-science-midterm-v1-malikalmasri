import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = round(math.pi * radius ** 2, 2)

    return area

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    space = ""
    result = ""

    if n <= 3:
        result = "The triangle height should be at least 4."
    
    else:
        result = "*\n**\n"

        for i in range(1, n - 2):
            space = " " * i
            result += "*" + space + "*\n"
        
        result += "*" * n

    return result.rstrip()

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    space = ""
    result = ""
    
    if n <= 2:
        result = "The pyramid height should be at least 3."
    
    else:
        for i in range(1, n + 2):
            space = " " * (i - 1)
            result += space + "*" * (2 * n - 2 * i + 1) + "\n"

    return result.rstrip()