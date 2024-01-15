#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter_content = file.read()

with open("./Input/Names/invited_names.txt", "r") as file:
    names_content = file.readlines()

name_list = []
for i in range(len(names_content)):
    name_list.append(names_content[i].strip())
    
for i in range(len(name_list)):
    letter_ready_to_send = letter_content.replace("[name]", name_list[i])
    
    with open(f"./Output/ReadyToSend/letter_for_{name_list[i]}.txt", "w") as file:
        letter_ready_to_send = file.write(letter_ready_to_send)