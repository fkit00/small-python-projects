import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data =pandas.read_csv("nato_phonetic_alphabet.csv")
# we want to use iterrows 
phonetic_dictionary={row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
# now we need to check against our dictionaru 
print([phonetic_dictionary[item] for item in word])

