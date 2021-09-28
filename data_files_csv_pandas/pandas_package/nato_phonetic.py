import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_map={row.letter:row.code for (index,row) in data.iterrows() }

name=input("what is your name?").upper()
phonetic_sequence=[phonetic_map[letter] for letter in name]
print(phonetic_sequence)