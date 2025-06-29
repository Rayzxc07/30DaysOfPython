import re
from collections import Counter

def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def most_frequent_words(text, top_n=3):
    words = text.split()
    counter = Counter(words)

    return [(count, word) for word, count in counter.most_common(top_n)]
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting 
&and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned = clean_text(sentence)
frequent = most_frequent_words(cleaned)
print(cleaned)
print(frequent)