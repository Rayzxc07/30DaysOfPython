def get_grade(score):
    """Assigns a letter grade based on a numerical score."""
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score <= 89:
        return "B"
    elif 60 <= score <= 69:
        return "C"
    elif 50 <= score <= 59:
        return "D"
    elif 0 <= score <= 49:
        return "F"
    else:
        return "Invalid score"

score = int(input("Enter the student's score: "))
grade = get_grade(score)
print(f"The grade is: {grade}")

def get_season(month):
    """Determines the season based on the month."""
    month = month.lower()
    if month in ["september", "october", "november"]:
        return "Autumn"
    elif month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    else:
        return "Invalid month"


month = input("Enter the month: ")
season = get_season(month)
print(f"The season is: {season}")

fruits = ['banana', 'orange', 'mango', 'lemon']

def manage_fruit_list(fruits, fruit):
    """Adds a fruit to the list if it doesn't already exist."""
    fruit = fruit.lower()
    if fruit in fruits:
        print('That fruit already exists in the list')
    else:
        fruits.append(fruit)
        print(f"Modified list: {fruits}")


new_fruit = input("Enter a fruit: ")
manage_fruit_list(fruits, new_fruit)