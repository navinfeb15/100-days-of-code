# Import the logo from art.py
from art import logo

# Define the list of letters in the alphabet, including duplicates at the beginning and end for handling shifts that go beyond z or before a
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Print the logo
print(logo)

# Define the caesar() function that takes in three parameters: the start text, shift amount, and cipher direction


def caesar(start_text, shift_amount, cipher_direction):
  # If the shift amount is greater than 26, use the modulus operator to wrap around to the beginning of the alphabet
  if shift_amount > 26:
    shift_amount %= 26
  # Initialize an empty string to hold the end text
  end_text = ""
  # If the cipher direction is decode, multiply the shift amount by -1 to reverse the direction of the cipher
  if cipher_direction == "decode":
    shift_amount *= -1
  # Loop through each character in the start text
  for char in start_text:
    # If the character is a letter, find its position in the alphabet and shift it by the shift amount
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    # If the character is not a letter, add it to the end text as is
    else:
      end_text += char
  # Print the final result, including the cipher direction and the end text
  print(f"Here's the {cipher_direction}d result: {end_text}")


# Initialize a boolean variable to control the while loop
exit = True
# Loop through the cipher program until the user chooses to exit
while exit:
  # Ask the user whether they want to encode or decode
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  # Ask the user for the message to be ciphered
  text = input("Type your message:\n").lower()
  # Ask the user for the shift amount
  shift = int(input("Type the shift number:\n"))

  # Call the caesar() function with the user's input as parameters
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  # Ask the user whether they want to start over
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  # If the user does not want to start over, set the exit variable to True to end the while loop and print a farewell message
  if again == "no":
    exit = False
    print("Goodbye..")
