import random
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

print(random_user_id())
import random
import string

def user_id_gen_by_user():
    """Generates user IDs based on user-specified length and quantity."""
    try:
        length = int(input("Enter the desired length of the user IDs: "))
        quantity = int(input("Enter the number of IDs to generate: "))

        if length <= 0 or quantity <= 0:
            return "Length and quantity must be positive integers."

        characters = string.ascii_letters + string.digits

        for _ in range(quantity):
            user_id = ''.join(random.choice(characters) for i in range(length))
            print(user_id)

    except ValueError:
        return "Invalid input. Please enter integers only."

print(user_id_gen_by_user())
print(user_id_gen_by_user())
import random

def rgb_color_gen():
    """Generates a random RGB color code."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())