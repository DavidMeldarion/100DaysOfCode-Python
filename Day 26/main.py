import pandas
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_data_frame = pandas.DataFrame(nato_csv)

# for (index, row) in nato_data_frame.iterrows():
#     print(index, row)

nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

print (nato_alphabet_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ")

coded_word = [nato_alphabet_dict[item.upper()] for (item) in word]

print(coded_word)
