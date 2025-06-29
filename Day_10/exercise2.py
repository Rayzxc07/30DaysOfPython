# DAY10 EXERCISE2

total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers from 0 to 100 is: {total_sum}")
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"The sum of all even numbers from 0 to 100 is: {sum_even}")
print(f"The sum of all odd numbers from 0 to 100 is: {sum_odd}")