# Day 8 exercise1
dog = {}

dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 3

student = {
    "first_name": "Raymart",
    "last_name": "Garcia",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "Java"],
    "country": "Philippines",
    "city": "Manila",
    "address": "123 Main St"
}

length = len(student)
print(f"Length of student dictionary: {length}")
skills = student["skills"]

print(f"Skills: {skills}, Data type: {type(skills)}")
student["skills"].extend(["C++", "SQL"])

print(f"Modified skills: {student['skills']}")
keys = list(student.keys())

print(f"Keys: {keys}")
values = list(student.values())

print(f"Values: {values}")
items = list(student.items())

print(f"Items as list of tuples: {items}")
del student["address"]

print(f"Student dictionary after deleting 'address': {student}")
del student