import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph.lower())

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print(sorted_words)
import re

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

numbers = re.findall(r'-?\d+', text)
points = list(map(int, numbers))
min_point = min(points)
max_point = max(points)

distance = max_point - min_point

print("Extracted numbers:", points)
print("Furthest points:", (min_point, max_point))
print("Distance:", distance)