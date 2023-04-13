# Name: Jeonghoo Lee
# SBUID: 115665774
##################### SCORE ######################
####### good work Score:  10/10
#################################################
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
    celcius = (5/9)*(fahrenheit - 32)
    return celcius

tempF = float(input('Enter the temperature in degrees Fahrenheit: '))
print('Temperature in degrees Celcius:', fahrenheit2celsius(tempF))

# Void function - as it only displays text on the screen and doesn't return a value
def what_to_wear(celsius):
    temp_range = (-10, 0, 10, 20)
    clothing = ('Puffy jacket', 'Scarf', 'Sweater', 'Light jacket', 'T-shirt')
    wear = []
    if celsius < -10:
        wear += [0]
    elif celsius > 20:
        wear += [4]
    else:
        for i in range(3):
            if temp_range[i] <= celsius <= temp_range[i+1]:
                wear += [i+1]
    if len(wear) == 2:
        print('You should wear a ' + clothing[wear[0]] + ', or a ' + clothing[wear[1]])
    else:
        print('You should wear a ' + clothing[wear[0]])
    
tempC = float(input('Enter the temperature in degrees Celsius: '))
what_to_wear(tempC)


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2)) / 2)

def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = euclidean_distance(x1, y1, x2, y2)
    s2 = euclidean_distance(x2, y2, x3, y3)
    s3 = euclidean_distance(x3, y3, x1, y1)
    return s1 + s2 + s3

x1 = float(input('Vertex 1 x-coordinate: '))
y1 = float(input('Vertex 1 y-coordinate: '))
x2 = float(input('Vertex 2 x-coordinate: '))
y2 = float(input('Vertex 2 y-coordinate: '))
x3 = float(input('Vertex 3 x-coordinate: '))
y3 = float(input('Vertex 3 y-coordinate: '))

print('Area of the triangle:', shoelace_triangle_area(x1, y1, x2, y2, x3, y3))
print('Perimeter of the triangle:', compute_triangle_perimeter(x1, y1, x2, y2, x3, y3))


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    return deg * math.pi / 180

def apothem(number_sides, length_side):
    return length_side / (2*math.tan(deg2rad(180/number_sides)))

def polygon_area(number_sides, length_side):
    return number_sides * length_side * apothem(number_sides, length_side) / 2

n = float(input('Enter the number of sides: '))
s = float(input('Enter the length of each side: '))
print('The area of the polygon is:', polygon_area(n, s))


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

