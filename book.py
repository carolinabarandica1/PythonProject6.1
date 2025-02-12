import requests

link = "https://www.gutenberg.org/files/84/84-0.txt"

result = requests.get(link)
text = result.text
unique_words = {}
punctuation = ",.'!?-=()"

for line in text.splitlines():
    for p in punctuation:
        line = line.replace(p, "")  # Correct placement of .replace()

    words = line.lower().split()
    for word in words:
        unique_words[word] = unique_words.get(word, 0) + 1

for word, count in list(unique_words.items())[:10]:
    print(f"{word}: {count}")


