#Random
import random

WORDS = ["MOTHER", "FATHER", "SISTER", "FAMILY"]
print(WORDS)
output = []
word = random.choice(WORDS)
while len(output) != len(WORDS):
    if word in output:
        word = random.choice(WORDS)
    else:
        output.append(word)
        word = random.choice(WORDS)
print(output)
input("\n\nPress ENTER to EXIT.")
