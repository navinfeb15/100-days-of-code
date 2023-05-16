import pandas as pd

data = pd.read_csv("Day-26/nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_words = list(input("Enter a word: "))
final_word = [new_dict[word.upper()] for word in user_words]

print(final_word)