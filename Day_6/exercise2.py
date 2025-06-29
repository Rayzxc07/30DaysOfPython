# Day 6 exercise 2
family_members = ('Calixto', 'Tessie', 'Ray', 'Mark')
father, mother, *siblings = family_members

print("Father:", father)
print("Mother:", mother)
print("Siblings:", siblings)

fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'lettuce', 'spinach')
animal_products = ('milk', 'egg', 'cheese')

food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp:", food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt:", food_stuff_lt)

length = len(food_stuff_lt)
if length % 2 == 0:
    middle_items = food_stuff_lt[length//2 - 1 : length//2 + 1]
else:
    middle_items = [food_stuff_lt[length//2]]

print("Middle item(s):", middle_items)
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print("First three items:", first_three)
print("Last three items:", last_three)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
