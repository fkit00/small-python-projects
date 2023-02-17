import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data =pandas.read_csv("nato_phonetic_alphabet.csv")
# we want to use iterrows 
phonetic_dictionary={row.letter:row.code for (index,row) in data.iterrows()}

def generate_phonetic (): 
    word = input("Enter a word: ").upper()
    try:
        output_list=[phonetic_dictionary[item] for item in word]
    except KeyError:
        print("Sorry only letters in the alphabet please")
        generate_phonetic() 
    else:
        print(output_list)

generate_phonetic()