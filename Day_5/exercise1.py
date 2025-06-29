# Day_5
empty_list = []

my_list = [10, 20, 30, 40, 50, 60, 70]

list_length = len(my_list)
print(f"Length of my_list: {list_length}")

first_item = my_list[0]
middle_index = len(my_list) // 2
middle_item = my_list[middle_index]
last_item = my_list[-1]
print(f"First: {first_item}, Middle: {middle_item}, Last: {last_item}")

mixed_data_types = ["Raymart",21,5.5, "Garcia", "Aringay"]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(f"\nIT Companies: {it_companies}")

num_companies = len(it_companies)
print(f"Number of companies: {num_companies}")

first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(f"First: {first_company}, Middle: {middle_company}, Last: {last_company}")

it_companies[0] = 'Meta'
print(f"\nModified list: {it_companies}")

it_companies.append('Salesforce')
print(f"List after appending: {it_companies}")

it_companies.insert(len(it_companies) // 2, 'Netflix')
print(f"List after inserting: {it_companies}")

it_companies[it_companies.index('Google')] = 'GOOGLE'
print(f"List after changing case: {it_companies}")

joined_companies = '#; '.join(it_companies)
print(f"\nJoined companies: {joined_companies}")

print(f"Does 'Apple' exist? {'Apple' in it_companies}")

it_companies.sort()
print(f"\nSorted list: {it_companies}")

it_companies.reverse()
print(f"Reversed list: {it_companies}")

first_three = it_companies[:3]
print(f"\nFirst three: {first_three}")

last_three = it_companies[-3:]
print(f"Last three: {last_three}")

middle_companies = it_companies[4:6]
print(f"Middle companies: {middle_companies}")

it_companies.pop(0)
print(f"\nList after removing first: {it_companies}")

it_companies.pop(len(it_companies)//2)
print(f"List after removing middle: {it_companies}")

it_companies.pop()
print(f"List after removing last: {it_companies}")

it_companies.clear()
print(f"List after removing all: {it_companies}")

it_companies = None

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
full_stack = joined_list.copy()
full_stack.insert(len(front_end), 'Python')
full_stack.insert(len(front_end) + 1, 'SQL')
print(f"\nFull stack: {full_stack}")