# Day 3 exercise
age = 21
height = 5.5
complex_number = 3 + 4j

base = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area = 0.5 * base * height_triangle
print("The area of the triangle is", area)

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area of the rectangle:", area_rectangle)
print("Perimeter of the rectangle:", perimeter_rectangle)

radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius * radius
circumference = 2 * pi * radius
print("Area of the circle:", area_circle)
print("Circumference of the circle:", circumference)

slope = 2
y_intercept = -2
x_intercept = 1
print("Slope:", slope)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope between points:", slope_points)
print("Euclidean distance:", distance)

print("Are the slopes equal?", slope == slope_points)
for x in range(-10, 10):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
    if y == 0:
        print(f"y is 0 when x = {x}")
len_python = len("python")
len_dragon = len("dragon")
print("Length of python:", len_python)
print("Length of dragon:", len_dragon)
print("Is length of python != dragon?", len_python != len_dragon)

print("'on' in python and dragon?", 'on' in 'python' and 'on' in 'dragon')

sentence = "I hope this course is not full of jargon."
print("'jargon' in sentence?", 'jargon' in sentence)

print("There is no 'on' in both dragon and python?", not ('on' in 'dragon' and 'on' in 'python'))

length_python = len('python')
length_float = float(length_python)
length_str = str(length_float)
print("Length as float:", length_float)
print("Length as string:", length_str)

number = int(input("Enter a number to check if it's even: "))
print("Is the number even?", number % 2 == 0)

print("Is 7 // 3 == int(2.7)?", 7 // 3 == int(2.7))

print("Is type('10') == type(10)?", type('10') == type(10))
try:
    print("Is int('9.8') == 10?", int('9.8') == 10)
except ValueError:
    print("Cannot convert '9.8' to int directly")

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print("Your weekly earning is", pay)

years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")