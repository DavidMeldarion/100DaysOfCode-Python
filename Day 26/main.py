"""NATO Alphabet converter"""
import pandas
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_data_frame = pandas.DataFrame(nato_csv)

nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

word = input("Enter a word: ")

coded_word = [nato_alphabet_dict[item.upper()] for item in word]

print(coded_word)
