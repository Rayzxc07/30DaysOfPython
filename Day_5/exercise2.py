import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")

ages.append(min_age)
ages.append(max_age)
print(f"Ages after adding min and max: {ages}")

median_age = statistics.median(ages)
print(f"Median age: {median_age}")

average_age = statistics.mean(ages)
print(f"Average age: {average_age}")

age_range = max_age - min_age
print(f"Range of ages: {age_range}")

min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print(f"Difference between min and average: {min_avg_diff}")
print(f"Difference between max and average: {max_avg_diff}")


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = [countries[middle_index]]
print(f"\nMiddle country(ies): {middle_countries}")

first_half_length = (len(countries) + 1) // 2
first_half = countries[:first_half_length]
second_half = countries[first_half_length:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

first_country, second_country, third_country, *scandic_countries = countries
print(f"\nFirst country: {first_country}")
print(f"Second country: {second_country}")
print(f"Third country: {third_country}")
print(f"Scandic countries: {scandic_countries}")