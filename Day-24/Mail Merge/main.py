with open("/workspaces/100-days-of-code/Day-24/Mail Merge/Input/Letters/starting_letter.txt", "r") as file:
    letter_text = file.read()

with open("/workspaces/100-days-of-code/Day-24/Mail Merge/Input/Names/invited_names.txt", "r") as file:
    names = [line.strip() for line in file.readlines()]

for name in names:
    letter = letter_text.replace("[name]", name)
    with open(f"/workspaces/100-days-of-code/Day-24/Mail Merge/Output/ReadyToSend/letter_for_{name}", "w") as file:
        file.write(letter)
