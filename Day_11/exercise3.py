def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def are_items_unique(data):
    """Checks if all items in a list are unique."""
    return len(data) == len(set(data))


def are_items_same_type(data):
    """Checks if all items in a list are of the same data type."""
    if not data:
        return True 
    return all(type(item) == type(data[0]) for item in data)


import keyword

def is_valid_variable_name(name):
    """Checks if a given string is a valid Python variable name."""
    if not isinstance(name, str):
        return False
    if not name.isidentifier():
        return False
    if keyword.iskeyword(name):
        return False
    return True

countries = {
    'USA': {'languages': ['English', 'Spanish'], 'population': 331000000},
    'India': {'languages': ['Hindi', 'English', 'Bengali'], 'population': 1380000000},
    'China': {'languages': ['Chinese'], 'population': 1450000000},
    'Brazil': {'languages': ['Portuguese'], 'population': 212000000},

}


def most_spoken_languages(data, top_n=10):
    """Returns the top N most spoken languages."""
    lang_counts = {}
    for country_data in data.values():
        for lang in country_data['languages']:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1

    sorted_langs = sorted(lang_counts.items(), key=lambda item: item[1], reverse=True)
    return [lang for lang, count in sorted_langs[:top_n]]


def most_populated_countries(data, top_n=10):
    """Returns the top N most populated countries."""
    sorted_countries = sorted(data.items(), key=lambda item: item[1]['population'], reverse=True)
    return [country for country, _ in sorted_countries[:top_n]]



print(f"Is '123' a valid variable name? {is_valid_variable_name('123')}") 
print(f"Is 'my_var' a valid variable name? {is_valid_variable_name('my_var')}") 
print(f"Is 'for' a valid variable name? {is_valid_variable_name('for')}") 
print(f"Are items unique? {are_items_unique([1,2,3,4])}")
print(f"Are items unique? {are_items_unique([1,2,3,2])}")
print(f"Are items same type? {are_items_same_type([1,2,3,4])}") 
print(f"Are items same type? {are_items_same_type([1,2,'a',4])}")
print(f"Is 7 prime? {is_prime(7)}")
print(f"Is 10 prime? {is_prime(10)}")

print(f"Most spoken languages in the world: {most_spoken_languages(countries, 5)}")
print(f"Most populated countries: {most_populated_countries(countries, 3)}")
