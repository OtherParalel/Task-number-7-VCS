import random

vowels = "aeiouy" # голосні літери
consonants = "bcdfghjklmnpqrstvwxz" # приголосні літери
def generate_good_word():
    length = random.randint(3, 8)
    word = random.choice(consonants).upper()

    for i in range(length - 1):

        if i % 2 == 0:
            word += random.choice(consonants)

        else:
            word += random.choice(vowels)
    return word
for i in range(10):
    print(generate_good_word())
