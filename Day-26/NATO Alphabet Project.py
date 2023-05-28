import pandas as pd

data = pd.read_csv("Day-26/nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def nato_phonetic_alphabet():
    user_words = list(input("Enter a word: "))
    try:
        final_word = [new_dict[word.upper()] for word in user_words]
        
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        nato_phonetic_alphabet()
    else:
        print(final_word)

nato_phonetic_alphabet()