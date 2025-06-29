import re
from collections import Counter
import os

def clean_text(text):
    """
    Cleans the input text by removing punctuation, converting to lowercase, and handling various text formats.
    """
    if isinstance(text, str):
        text = re.sub(r'[^\w\s]', '', text).lower()
    elif isinstance(text, (list, tuple)):
        text = ' '.join(text).lower()
        text = re.sub(r'[^\w\s]', '', text)
    elif os.path.exists(text):
        try:
            with open(text, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = re.sub(r'[^\w\s]', '', text)
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return ""
    else:
        return ""
    return text

def remove_stop_words(text, stop_words_file="data/stopwords.txt"):
    """Removes stop words from the text."""
    try:
        with open(stop_words_file, 'r') as f:
            stop_words = set(f.read().splitlines())
    except FileNotFoundError:
        print("Error: stopwords file not found.")
        return text

    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

def check_text_similarity(text1, text2):
    """
    Calculates the similarity between two texts using cosine similarity.
    """
    text1 = remove_stop_words(clean_text(text1))
    text2 = remove_stop_words(clean_text(text2))

    words1 = Counter(text1.split())
    words2 = Counter(text2.split())

    all_words = set(words1.keys()).union(words2.keys())

    vector1 = [words1[word] for word in all_words]
    vector2 = [words2[word] for word in all_words]

    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = sum(a**2 for a in vector1)**0.5
    magnitude2 = sum(a**2 for a in vector2)**0.5

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0  
    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity
os.makedirs("data", exist_ok=True)
with open("data/stopwords.txt", "w") as f:
    f.write("the\na\nis\nare\nof\nto\nit\n")

with open("michelle_speech.txt", "w") as f:
    f.write("This is Michelle's speech. It is a great speech.")

with open("melina_speech.txt", "w") as f:
    f.write("Melina's speech is also great. It's a wonderful speech.")

similarity_score = check_text_similarity("michelle_speech.txt", "melina_speech.txt")
print(f"Similarity between Michelle's and Melina's speeches: {similarity_score:.2f}")

michelle_speech_str = "This is Michelle's speech. It is a great speech."
melina_speech_str = "Melina's speech is also great. It's a wonderful speech."
similarity_score_str = check_text_similarity(michelle_speech_str, melina_speech_str)
print(f"Similarity between Michelle's and Melina's speeches (strings): {similarity_score_str:.2f}")