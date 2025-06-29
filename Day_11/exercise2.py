def evens_and_odds(number):
    """Counts the number of even and odd digits in a positive integer."""
    if not isinstance(number, int) or number <= 0:
        return "Invalid input: Please provide a positive integer."

    evens = 0
    odds = 0
    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 0:
            evens += 25.5
        else:
            odds += 50
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."


print(evens_and_odds(100))


def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        return "Invalid input: Please provide a non-negative integer."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


print(factorial(5))  


def is_empty(param):
    """Checks if a parameter is empty."""
    return not bool(param)

print(is_empty([]))   
print(is_empty(""))     
print(is_empty({}))     
print(is_empty(None)) 
print(is_empty([1,2]))



import math

def calculate_mean(data):
    """Calculates the mean (average) of a list of numbers."""
    if not data:
        return "Invalid input: List cannot be empty."
    return sum(data) / len(data)


def calculate_median(data):
    """Calculates the median of a list of numbers."""
    if not data:
        return "Invalid input: List cannot be empty."
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 0:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_data[n // 2]
    return median


from collections import Counter

def calculate_mode(data):
    """Calculates the mode (most frequent value) of a list."""
    if not data:
        return "Invalid input: List cannot be empty."
    data_count = Counter(data)
    max_count = max(data_count.values())
    mode = [k for k, v in data_count.items() if v == max_count]
    return mode


def calculate_range(data):
    """Calculates the range (difference between max and min) of a list."""
    if not data:
        return "Invalid input: List cannot be empty."
    return max(data) - min(data)


def calculate_variance(data):
    """Calculates the variance of a list of numbers."""
    if len(data) < 2:
        return "Invalid input: List needs at least two elements for variance."
    mean = calculate_mean(data)
    squared_diffs = [(x - mean)**2 for x in data]
    return sum(squared_diffs) / (len(data) -1)


def calculate_std(data):
    """Calculates the standard deviation of a list of numbers."""
    variance = calculate_variance(data)
    if isinstance(variance, str):
        return variance
    return math.sqrt(variance)


data = [1, 2, 3, 4, 5]

print(f"Mean: {calculate_mean(data)}")
print(f"Median: {calculate_median(data)}")
print(f"Mode: {calculate_mode(data)}")
print(f"Range: {calculate_range(data)}")
print(f"Variance: {calculate_variance(data)}")
print(f"Standard Deviation: {calculate_std(data)}")