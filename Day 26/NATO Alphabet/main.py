import pandas

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# my way↧
# get the csv data
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic = []
name = input("Enter your name: ").upper()
split_name = [letter for letter in name]
for letter in split_name:
    for (index, row) in data.iterrows():
        if row.letter == letter:
            nato_phonetic.append(row.code)
            print(f"your nato phonetic alphabet are: {letter} {row.code}")
print(nato_phonetic)


# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# # course way↧
# # TODO 1. Create a dictionary in this format:
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# name = input("Enter your name: ").upper()
# output_list = [phonetic_dict[letter] for letter in name]
# print(output_list)


