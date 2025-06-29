#Day14ex1
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()
def square(x):
    return x * x
def is_even(x):
    return x % 2 == 0
from functools import reduce
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]

mapped = list(map(square, numbers))
filtered = list(filter(is_even, numbers))
reduced = reduce(add, numbers)

print(mapped)
print(filtered)
print(reduced)

countries = ['Kenya', 'Canada', 'Brazil']
names = ['Alice', 'Bob', 'Charlie']
numbers = [10, 20, 30, 40]

for country in countries:
    print(country)

for name in names:
    print(name)
for number in numbers:
    print(number)