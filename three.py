loving_words = ['Sweetheart', 'Honey', 'Darling', 'Love', 'Baby','Sweetie', 'Dearest', 'Angel', 'Cupid',
                'Beloved', 'Dear', 'Cherub', 'Babe','My darling', 'Sugar', 'Precious','Adore', 'Heartthrob', 'My dear']
def is_loving_word(word):
    if word in loving_words:
        return True
    else:
        return False

user_input = input("Enter a word: ")
if is_loving_word(user_input):
    print("That's a loving word!")
else:
    print("That's not a loving word.")
