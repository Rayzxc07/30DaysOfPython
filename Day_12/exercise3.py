#Day12 exercise 3
import random

def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list
my_list = [1, 2, 3, 4, 5]
print(shuffle_list(my_list))
import random

def unique_random_numbers():
    return random.sample(range(10), 7)
print(unique_random_numbers())