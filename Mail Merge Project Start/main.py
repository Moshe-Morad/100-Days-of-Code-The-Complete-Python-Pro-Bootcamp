# TODO: Create a letter using starting_letter.txt
# TODO: for each name in invited_names.txt
# TODO: Replace the [name] placeholder with the actual name.
# TODO: Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_template:
    letter = letter_template.read()

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/{name}.docx", mode="w") as new_letter_for:
            new_letter_for.write(new_letter)

