import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = {
    "Research Expenditures": "$554.0 M",
    "Study Abroad Programs": "200+",
    "Sponsored Research Awards": "$645.6 M",
    "Student Body": {
        "Total Students": 37557,
        "Living Alumni": "431,000+",
        "Total Employees": 10674,
        "Faculty": 4309,
        "Nondegree Students": 1337,
        "Graduate & Professional Students": 18476,
        "Undergraduate Students": 17744
    },
    "Campus": {
        "Classrooms": 848,
        "Buildings": 343,
        "Laboratories": 1481,
        "Libraries": 13,
        "Campus Area (acres)": 140
    },
    "Academics": {
        "Study Abroad Programs": "80+",
        "Average Class Size": 30,
        "Student/Faculty Ratio": "11:1",
        "Schools and Colleges": 17,
        "Programs of Study": "300+"
    }
}

with open('bu_facts_stats.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been scraped and saved to bu_facts_stats.json")

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve the webpage: {response.status_code}")
    exit()
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

tables = soup.find_all('table')

if not tables:
    print("No tables found on the webpage.")
    exit()

table = tables[0]
headers = [header.text.strip() for header in table.find_all('th')]

data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if cols:
        data.append([col.text.strip() for col in cols])

df = pd.DataFrame(data, columns=headers)
json_data = df.to_json(orient='records', lines=False)

with open('uci_datasets.json', 'w') as json_file:
    json_file.write(json_data)

print("Data has been scraped and saved to uci_datasets.json")

import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_presidents():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', {'class': 'wikitable'})
    
    presidents = []
    
    for row in table.find_all('tr')[1:]:
        cells = row.find_all(['th', 'td'])
        
        if len(cells) < 8:
            continue
            
        number = cells[0].get_text().strip()
        name_cell = cells[2]
        name = name_cell.get_text().strip()
        name = re.sub(r'\[\d+\]', '', name).strip()
        name_parts = name.split(' ')
        first_name = name_parts[0]
        last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''
        
        name_link = name_cell.find('a')
        wikipedia_url = f"https://en.wikipedia.org{name_link['href']}" if name_link else None
        
        term = cells[3].get_text().strip()
        term_dates = term.split('–')
        term_start = term_dates[0].strip() if len(term_dates) > 0 else ''
        term_end = term_dates[1].strip() if len(term_dates) > 1 else ''
        
        party = cells[5].get_text().strip().split('[')[0]
        party = re.sub(r'\[\d+\]', '', party).strip()
        
        election = cells[6].get_text().strip()
        vice_president = cells[7].get_text().strip()
        vice_president = re.sub(r'\[\d+\]', '', vice_president).strip()
        
        president_data = {
            "number": number,
            "name": name,
            "first_name": first_name,
            "last_name": last_name,
            "wikipedia_url": wikipedia_url,
            "term": term,
            "term_start": term_start,
            "term_end": term_end,
            "party": party,
            "election": election,
            "vice_president": vice_president
        }
        
        presidents.append(president_data)
    
    return presidents

presidents_data = scrape_presidents()
with open('us_presidents.json', 'w') as f:
    json.dump(presidents_data, f, indent=2)

print(f"Scraped data for {len(presidents_data)} presidents and saved to us_presidents.json")