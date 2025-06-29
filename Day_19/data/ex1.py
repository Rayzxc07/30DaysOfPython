def count_lines_and_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            return num_lines, num_words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0, 0

speech_files = {
    "Obama": "data/obama_speech.txt",
    "Michelle Obama": "data/michelle_obama_speech.txt",
    "Donald Trump": "data/donald_speech.txt",
    "Melina Trump": "data/melina_trump_speech.txt"
}
for speaker, file_path in speech_files.items():
    lines, words = count_lines_and_words(file_path)
    print(f"{speaker} Speech:")
    print(f"  Number of lines: {lines}")
    print(f"  Number of words: {words}\n")


    import json
from collections import Counter

def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    language_counts = Counter()
    for country in countries:
        for language in country.get('languages', []):
            language_counts[language] += 1

    most_common = language_counts.most_common(top_n)

    return [(count, lang) for lang, count in most_common]

print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))
print(most_spoken_languages(filename='./data/countries_data.json', top_n=3))

import json

def most_populated_countries(filename, top_n):

    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    population_data = [
        {'country': country['name'], 'population': country['population']}
        for country in countries
    ]

    sorted_population = sorted(population_data, key=lambda x: x['population'], reverse=True)

    return sorted_population[:top_n]

print(most_populated_countries('./data/countries_data.json', 10))
print(most_populated_countries('./data/countries_data.json', 3))
