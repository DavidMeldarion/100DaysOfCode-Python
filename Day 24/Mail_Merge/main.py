#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("./Mail_Merge/Input/Names/invited_names.txt") as invited_names_file:
    invited_names = invited_names_file.readlines()
    print (invited_names)
for name in invited_names:
    with open("./Mail_Merge/Input/Letters/starting_letter.txt", "r") as starting_letter_file:
        contents=starting_letter_file.readlines()
        name_strip=name.strip("\n")
        contents[0] = contents[0].replace("[name]", name_strip)
        contents_string="".join(contents)
        print(contents_string)
        filename = f"./Mail_Merge/Output/ReadyToSend/letter_for_{name_strip.lower()}"
        with open(filename, "w+") as final_letter:
            final_letter.write(contents_string)
