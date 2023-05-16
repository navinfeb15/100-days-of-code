#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
# names = []
with open("/workspaces/100-days-of-code/Day-24/Mail Merge/Input/Letters/starting_letter.txt", "r") as file:
    letter_text = file.read()
# print(letter_text)

with open("/workspaces/100-days-of-code/Day-24/Mail Merge/Input/Names/invited_names.txt","r") as file:
    names = [line.strip() for line in file.readlines()]
#Replace the [name] placeholder with the actual name.

for name in names:
    letter = letter_text.replace("[name]", name)
    with open(f"/workspaces/100-days-of-code/Day-24/Mail Merge/Output/ReadyToSend/letter_for_{name}","w") as file:
        file.write(letter)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp