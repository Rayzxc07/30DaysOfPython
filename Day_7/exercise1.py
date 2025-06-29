# Day7 exercise 1
it_companies = {'Google', 'Microsoft', 'Apple', 'Facebook'}
num_companies = len(it_companies)
print(f"The number of IT companies in the set is: {num_companies}")
it_companies.add('Twitter')
print(it_companies)

new_companies = ['Amazon', 'IBM', 'Salesforce']
it_companies.update(new_companies)
print(it_companies)

it_companies.remove('Facebook')
print(it_companies)

it_companies.discard('Google')
print(it_companies)