# Day 7 exercise 3
ages_list = [25, 30, 25, 35, 40, 30, 25]
ages_set = set(ages_list)
list_length = len(ages_list)
set_length = len(ages_set)
print(f"Length of the list: {list_length}")
print(f"Length of the set: {set_length}")
if list_length > set_length:
    print("The list is bigger.")
else:
    print("The set is bigger or they are equal.")