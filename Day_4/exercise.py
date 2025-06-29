string1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(string1)

company = "Coding For All"
new_company = company.replace('Coding', 'Python')
print(new_company)
another_string = 'Python for Everyone'
print(another_string.replace('Everyone', 'All'))
words = company.split()
print(words)
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list = companies.split(',')
print(company_list)
print(company[0])
print(company[-1])

acronym1 = "PFE"
acronym2 = "CFA"
print(acronym1)
print(acronym2)

print(company.index('C'))
print(company.index('F'))

sentence = 'Coding For All People'
print(sentence.rfind('l'))

sentence2 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence2.index('because'))
print(sentence2.rindex('because'))
print(sentence2[31:51])

print(sentence2.find('because'))
print(sentence2[31:51]) 
print(company.startswith('Coding'))
print(company.endswith('coding'))  

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 * 6 = {8 ** 6}")