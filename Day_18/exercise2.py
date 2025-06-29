import re
def is_valid_variable(name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, name) is not None
print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))   