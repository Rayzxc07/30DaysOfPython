#Day13 exercise1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_or_zero = [num for num in numbers if num <= 0]
print(f"Negative or zero numbers: {negative_or_zero}")

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(f"Flattened list: {flattened_list}")


list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(f"List of tuples: {list_of_tuples}")


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_uppercase = [[country.upper(), country[:3].upper(), city.upper()] for country, city in [item for sublist in countries for item in sublist]]
print(f"Uppercase countries: {countries_uppercase}")


countries_dict = [{'country': country.upper(), 'city': city.upper()} for country, city in [item for sublist in countries for item in sublist]]
print(f"Countries as dictionaries: {countries_dict}")


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for name in [item for sublist in names for item in sublist]]
print(f"Concatenated names: {concatenated_names}")

slope_intercept = lambda x1, y1, x2, y2: (
    (y2 - y1) / (x2 - x1) if x2 != x1 else "Undefined slope (vertical line)",
    y1 - ((y2 - y1) / (x2 - x1)) * x1 if x2 != x1 else "Undefined y-intercept"

)
slope, intercept = slope_intercept(1, 2, 3, 4) 
print(f"Slope: {slope}, Intercept: {intercept}")

slope, intercept = slope_intercept(2, 4, 2, 6)
print(f"Slope: {slope}, Intercept: {intercept}")