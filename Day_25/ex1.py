import pandas as pd

df = pd.read_csv(r'hacker_news.csv')
print(df)

print("First five rows:")
print(df.head())

print("\nLast five rows:")
print(df.tail())

print("\nTitle column:")
titles = df['title']
print(titles)

print("\nShape of the dataset:")
print(df.shape)

print("\nTitles containing 'python':")
python_titles = df[df['title'].str.contains('python', case=False, na=False)]
print(python_titles['title'])

print("\nTitles containing 'JavaScript':")
js_titles = df[df['title'].str.contains('javascript', case=False, na=False)]
print(js_titles['title'])

print("\nSummary statistics:")
print(df.describe(include='all'))

print("\nNull values per column:")
print(df.isnull().sum())

print("\nUnique titles count:")
print(df['title'].nunique())