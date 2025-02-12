from enum import unique
from string import punctuation

import requests

link = "https://gutenberg.org/cache/epub/84/pg84"

result = requests.get(link)
unique_words = {}
punctuation = ",.'!?-=()"
print(result.text)

for line in result.text.splitlines():
    print()