def add_two_numbers(x, y):
    """Returns the sum of two numbers."""
    return x + y

print(add_two_numbers(3, 5))
import math

def area_of_circle(r):
    """Calculates the area of a circle given radius r."""
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r ** 2

print(area_of_circle(4))
def add_all_nums(*args):
    """Sums all numeric arguments; raises TypeError for non-numbers."""
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            raise TypeError(f"All arguments must be numbers. Got {type(num)}")
        total += num
    return total

print(add_all_nums(1, 2, 3.5))
def convert_celsius_to_fahrenheit(celsius):
    """Converts Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

print(convert_celsius_to_fahrenheit(25))

def check_season(month):
    """Returns the season for a given month (case-insensitive)."""
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'

print(check_season('October'))
def calculate_slope(x1, y1, x2, y2):
    """Calculates slope between two points (x1,y1) and (x2,y2)."""
    if x1 == x2:
        raise ValueError("Slope is undefined (vertical line)")
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(1, 2, 3, 4))
import cmath

def solve_quadratic_eqn(a, b, c):
    """Returns both solutions to ax² + bx + c = 0."""
    discriminant = (b ** 2) - (4 * a * c)
    x1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    x2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    return x1, x2

print(solve_quadratic_eqn(1, -3, 2))
def print_list(lst):
    """Prints each list element on a new line."""
    for item in lst:
        print(item)

print_list(['apple', 'banana', 'cherry'])

def reverse_list(arr):
    """Returns a reversed version of the input list using loops."""
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))
def capitalize_list_items(lst):
    """Returns a new list with all items capitalized."""
    return [item.capitalize() for item in lst]

print(capitalize_list_items(['apple', 'banana', 'cherry']))
def add_item(lst, item):
    """Adds an item to the end of a list and returns the modified list."""
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
def add_item(lst, item):
    """Adds an item to the end of a list and returns the modified list."""
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
def remove_item(lst, item):
    """Removes an item from a list and returns the modified list."""
    if item in lst:
        lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))
def sum_of_numbers(n):
    """Returns the sum of all numbers from 1 to n."""
    return sum(range(1, n+1))

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))
def sum_of_odds(n):
    """Returns the sum of all odd numbers from 1 to n."""
    return sum(i for i in range(1, n+1) if i % 2 != 0)

print(sum_of_odds(5))
print(sum_of_odds(10))
def sum_of_even(n):
    """Returns the sum of all even numbers from 1 to n."""
    return sum(i for i in range(1, n+1) if i % 2 == 0)

print(sum_of_even(5))
print(sum_of_even(10))
