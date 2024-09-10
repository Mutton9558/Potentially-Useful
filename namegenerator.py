import random
# name generator
vowel = "aeiou"
consonant = "abcdefghijklmnopqrstuvwxyz"
COUNTER = 2

vowel = [v for v in vowel]
consonant = [c for c in consonant if c not in vowel]

name = []
for i in range(5 + random.randint(-COUNTER, COUNTER)):
    cran = random.randint(0, len(consonant)-1)
    name.append(consonant[cran])
    vran = random.randint(0, len(vowel)-1)
    name.append(vowel[vran])

name = ''.join(name)
print(f"Your auto-generated name is {name}")
