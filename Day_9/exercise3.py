person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print(f"The middle skill is: {middle_skill}")

if 'skills' in person:
  if 'Python' in person['skills']:
    print("The person has Python skill.")
  else:
    print("The person does not have Python skill.")

skills = person.get('skills', [])

if skills == ['JavaScript', 'React']:
    print('He is a front end developer')
elif set(['Node', 'Python', 'MongoDB']).issubset(set(skills)):
    print('He is a backend developer')
elif set(['React', 'Node', 'MongoDB']).issubset(set(skills)):
    print('He is a fullstack developer')
else:
    print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")