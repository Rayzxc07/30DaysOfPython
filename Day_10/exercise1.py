# DAY 10
print("Iterating from 0 to 10:")
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1
print("\nIterating from 10 to 0:")
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1
print("\nTriangle:")
for i in range(1, 8):
    print("#" * i)

print("\n8x8 grid:")
for i in range(8):
    print(" # " * 8)

print("\nMultiplication table:")
for i in range(11):
    print(f"{i} x {i} = {i*i}")

print("\nList iteration:")
for item in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(item)

print("\nEven numbers:")
for i in range(0, 101, 2):
    print(i)

print("\nOdd numbers:")
for i in range(1, 101, 2):
    print(i)