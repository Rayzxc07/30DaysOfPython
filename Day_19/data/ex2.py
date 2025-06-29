import re
from collections import Counter

def find_most_common_words(text_source, num_words):
    """
    Finds the most common words in a text file or string.

    Args:
        text_source: Path to a text file or a string containing text.
        num_words: The number of most common words to return.

    Returns:
        A list of tuples, where each tuple contains (count, word), sorted in descending order 
        of count.  Returns an empty list if the input is invalid or contains no words.
    """
    try:
        if isinstance(text_source, str):
            try:
                with open(text_source, 'r', encoding='utf-8') as file:
                    text = file.read()
            except FileNotFoundError:
                return []
        elif isinstance(text_source, (list,tuple)):
            text = ' '.join(text_source)
        else:
            text = str(text_source)
        
        text = re.sub(r'[^\w\s]', '', text).lower()
        words = text.split()

        if not words:
            return []

        word_counts = Counter(words)
        most_common = word_counts.most_common(num_words)

        return most_common

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

with open('sample.txt', 'w') as f:
    f.write("The quick brown fox jumps over the lazy dog. The dog barks at the fox. Be quick be quick. To be or not to be, that is the question. Of all the things, and and and.  I have a dream.")


print(find_most_common_words('sample.txt', 10))
print(find_most_common_words('sample.txt', 5))
print(find_most_common_words("This is a test string. This string is a test.",5))
print(find_most_common_words(["This", "is", "a", "test", "This", "is", "a", "test"],3))
print(find_most_common_words(123, 5))
print(find_most_common_words("nonexistent_file.txt",5))


import re
from collections import Counter
import os

obama_text = """
Thank you. Thank you so much. Tonight, more than 200 years after a former colony won the right to determine its own destiny,
the election of Barack Obama as President marks a defining moment in history. Change has come to America.
"""

michelle_text = """
As a mother, as a wife, as a human being, I am here tonight because I love this country.
We know what our kids deserve and we will keep working to build a future that is worthy of their dreams.
"""

trump_text = """
Thank you very much, everybody. Together, we will make America strong again. We will make America proud again.
We will make America safe again. And we will make America great again.
"""

melina_text = """
My husband has been fighting for you and our country. He will not stop until he has done all he can to make sure your families are safe,
your jobs are secure, and your future is bright. Thank you for your love and support.
"""
speeches = {
    "obama_speech.txt": obama_text,
    "michelle_obama_speech.txt": michelle_text,
    "trump_speech.txt": trump_text,
    "melina_trump_speech.txt": melina_text,
}

for filename, content in speeches.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def find_most_common_words(text_or_file, n):
    if os.path.isfile(text_or_file):
        with open(text_or_file, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        text = text_or_file

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    word_counts = Counter(words)

    most_common = word_counts.most_common(n)

    return [(count, word) for word, count in most_common]
print("\n Obama:")
print(find_most_common_words("obama_speech.txt", 10))

print("\n Michelle:")
print(find_most_common_words("michelle_obama_speech.txt", 10))

print("\n Trump:")
print(find_most_common_words("trump_speech.txt", 10))

print("\n Melina:")
print(find_most_common_words("melina_trump_speech.txt", 10))

from collections import Counter
import re
with open('romeo_and_juliet.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()
words = re.findall(r'\b\w+\b', text)
word_counts = Counter(words)
most_common = word_counts.most_common(10)

print("Top 10 most repeated words:")
for word, count in most_common:
    print(f"{word}: {count}")

import csv

def count_keywords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)

        python_count = 0
        js_count = 0
        java_only_count = 0

        for row in reader:
            line = ' '.join(row).lower()
            if 'python' in line:
                python_count += 1

            if 'javascript' in line:
                js_count += 1

            if 'java' in line and 'javascript' not in line:
                java_only_count += 1

        return python_count, js_count, java_only_count
if __name__ == '__main__':
    file_path = './data/hacker_news.csv'
    python_count, js_count, java_only_count = count_keywords(file_path)

    print(f"a) Lines containing Python: {python_count}")
    print(f"b) Lines containing JavaScript: {js_count}")
    print(f"c) Lines containing Java (but not JavaScript): {java_only_count}")