age = 21
print(f"Integer: {age}, Type: {type(age)}")

price = 99.99
print(f"Float: {price}, Type: {type(price)}")

complex_num = 2 + 3j
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

name = "Raymart"
print(f"String: {name}, Type: {type(name)}")

is_adult = True
print(f"Boolean: {is_adult}, Type: {type(is_adult)}")

shopping_list = ["milk", "eggs", "bread"]
print(f"List: {shopping_list}, Type: {type(shopping_list)}")

coordinates = (10, 20)
print(f"Tuple: {coordinates}, Type: {type(coordinates)}")

unique_numbers = {1, 2, 2, 3, 4}
print(f"Set: {unique_numbers}, Type: {type(unique_numbers)}")

person = {"Raymart": "Garcia", "age": 21, "city": "Philippines"}
print(f"Dictionary: {person}, Type: {type(person)}")

import math

def euclidean_distance(point1, point2):
    """Calculates the Euclidean distance between two points."""
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

point1 = (2, 3)
point2 = (10,8)

distance = euclidean_distance(point1, point2)
print(f"\nEuclidean distance between {point1} and {point2}: {distance}")