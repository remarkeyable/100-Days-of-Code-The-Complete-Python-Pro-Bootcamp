import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic = {row.letter:row.code for (index,row) in df.iterrows()}
word = input("Enter a word: ").upper()
result = [phonetic[letter] for letter in word]
print(result)
