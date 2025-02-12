d = {}

eng_to_spa = {"one": "uno", "two": "dos","three":"tres"}
print(eng_to_spa)
eng_to_spa["i"] = "yo"
eng_to_spa["am"]="soy"
eng_to_spa["spanish"]="español"
print(eng_to_spa)

sentence = "i am spanish"
words= sentence.split()

for word in words:
    print(eng_to_spa[word])

eng_to_spa.update({"yes":"si", "no":"no"})

print(eng_to_spa)
del eng_to_spa["no"]
print(eng_to_spa)