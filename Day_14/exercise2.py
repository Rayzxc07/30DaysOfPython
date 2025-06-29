countries = [
    'Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland',
    'Ireland', 'Spain', 'Italy', 'Poland', 'Germany', 'Ethiopia',
    'Australia', 'Austria', 'Pakistan', 'Kazakhstan'
]

from functools import reduce
uppercase_countries = list(map(str.upper, countries))
print(uppercase_countries)

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

names = ['Miya', 'Layla', 'Bruno']
uppercase_names = list(map(str.upper, names))
print(uppercase_names)

land_countries = list(filter(lambda country: 'land' in country, countries))
print(land_countries)

six_letter_countries = list(filter(lambda country: len(country) == 6, countries))
print(six_letter_countries)

six_or_more = list(filter(lambda country: len(country) >= 6, countries))
print(six_or_more)

starts_with_e = list(filter(lambda country: country.startswith('E'), countries))
print(starts_with_e)

numbers = [1, 2, 3, 4, 5, 6]
result = reduce(
    lambda acc, val: acc + val,
    filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers))
)
print(result)

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed_list = ['hello', 5, True, 'world']
print(get_string_lists(mixed_list))

total = reduce(lambda acc, val: acc + val, numbers)
print(total)

sentence = reduce(lambda acc, country: acc + ', ' + country, countries[:-1])
sentence += f", and {countries[-1]} are north European countries."
print(sentence)

def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country.lower(), countries))

print(categorize_countries('land'))
print(categorize_countries('ia'))

def country_stats_by_letter(countries_list):
    stats = {}
    for country in countries_list:
        first_letter = country[0].upper()
        stats[first_letter] = stats.get(first_letter, 0) + 1
    return stats

print(country_stats_by_letter(countries))

def get_first_ten_countries():
    return countries[:10]

print(get_first_ten_countries())

def get_last_ten_countries():
    return countries[-10:]
print(get_last_ten_countries())