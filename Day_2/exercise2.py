# Day 2 exercise2
first_name = "Raymart"
last_name = "Garcia"
full_name = "Raymart Garcia"
country = "Philippines" 
city = "Manila"
age = 21
year = 2003
is_married = True
is_true = True
is_light_on = False
x, y, z = 1, 2, 3

print("Data Types:")
print(f"first_name: {type(first_name)}")
print(f"last_name: {type(last_name)}")
print(f"full_name: {type(full_name)}")
print(f"country: {type(country)}")
print(f"city: {type(city)}")
print(f"age: {type(age)}")
print(f"year: {type(year)}")
print(f"is_married: {type(is_married)}")
print(f"is_true: {type(is_true)}")
print(f"is_light_on: {type(is_light_on)}")
print(f"x: {type(x)}")
print(f"y: {type(y)}")
print(f"z: {type(z)}")

print("\nLength of first name:", len(first_name))

print("\nComparison of name lengths:", len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("\nArithmetic Results:")
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

import math

radius = 30
area_of_circle = math.pi * radius**2
circum_of_circle = 2 * math.pi * radius

print("\nCircle Calculations (radius = 30):")
print("Area:", area_of_circle)
print("Circumference:", circum_of_circle)

radius = float(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius**2
print("\nCircle Area (user input):", area_of_circle)

first_name = input("Raymart: ")
last_name = input("Garcia: ")
country = input("Philippines: ")
age = int(input("21: "))

print("\nUser Information:")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

help('keywords')