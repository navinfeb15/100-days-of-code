from art import logo

# Define functions for addition, subtraction, multiplication, and division


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Create a dictionary mapping operator symbols to functions
calc_dict = {"+": add, "-": sub, "*": multiply, "/": divide}

# Define a function to run the calculator


def calc():
    print(logo)
    # Prompt user for the first number
    num1 = float(input("\nEnter the first number. \n"))
    print("Choose any of the following operations")
    # Print the available operators
    for key in calc_dict:
        print(key)

    end = False
    while not end:
        # Prompt user for the operator symbol
        operation_symbol = input("-"*34 + "\nPick an operation : ")
        # Prompt user for the second number
        num2 = int(input("Enter another number. \n"))
        # Calculate the result using the selected operator function
        answer = calc_dict[operation_symbol](num1, num2)
        # Print the result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Prompt user to continue with the same number or start with a new number or stop the program
        continue_again = input(
            "-"*34 + "\nPress 'y' to continue with the same number, 'n' to start with a new number, 'n' to stop the program...\n")
        if continue_again == 'y':
            # If user wants to continue with the same number, update answer to num1
            answer = num1
        elif continue_again == 'n':
            # If user wants to start with a new number, call the calc function recursively
            calc()
        else:
            # If user wants to stop the program, set end flag to True
            end = True


# Call the calc function to start the program
calc()
