import requests
from collections import Counter
import re
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
text = response.text
words = re.findall(r'\b\w+\b', text.lower())
word_counts = Counter(words)
most_common_10 = word_counts.most_common(10)
for word, freq in most_common_10:
    print(f'{word}: {freq}')
import requests
import statistics
from collections import Counter
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats = response.json()
print("API status code:", response.status_code)
print("Number of cat breeds loaded:", len(cats))
def parse_range(s):
    parts = s.split(' - ')
    return float(parts[0]), float(parts[1])
weights = []
lifespans = []
breed_countries = []
for cat in cats:
    try:
        min_w, max_w = parse_range(cat['weight']['metric'])
        avg_w = (min_w + max_w) / 2
        weights.append(avg_w)
    except:
        pass
    try:
        min_l, max_l = parse_range(cat['life_span'])
        avg_l = (min_l + max_l) / 2
        lifespans.append(avg_l)
    except:
        pass
    country = cat.get('origin', 'Unknown')
    breed = cat.get('name', 'Unknown')
    breed_countries.append((country, breed))
def describe(data, label):
    if not data:
        print(f"\nNo data for {label}.")
        return
    print(f"\n{label} stats:")
    print(f"- Min: {min(data):.2f}")
    print(f"- Max: {max(data):.2f}")
    print(f"- Mean: {statistics.mean(data):.2f}")
    print(f"- Median: {statistics.median(data):.2f}")
    print(f"- Std Dev: {statistics.stdev(data):.2f}")

describe(weights, "Weight (kg)")
describe(lifespans, "Lifespan (years)")

countries = [c[0] for c in breed_countries]
country_counts = Counter(countries)

print("\nBreed count by country:")
for country, count in country_counts.items():
    print(f"{country}: {count}")

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
datasets = []
for entry in soup.select('table.dataset-table tr'):
    name = entry.select_one('td:nth-child(1) a').text.strip()
    description = entry.select_one('td:nth-child(2)').text.strip()
    attributes = {
        'Instances': entry.select_one('td:nth-child(3)').text.strip(),
        'Features': entry.select_one('td:nth-child(4)').text.strip(),
        'Task': entry.select_one('td:nth-child(5)').text.strip()
    }
    datasets.append({'Name': name, 'Description': description, **attributes})

print("Top 5 Datasets from UCI Repository:")
for idx, dataset in enumerate(datasets[:5], 1):
    print(f"\n{idx}. {dataset['Name']}")
    print(f"   Description: {dataset['Description']}")
    print(f"   Instances: {dataset['Instances']}, Features: {dataset['Features']}, Task: {dataset['Task']}")
