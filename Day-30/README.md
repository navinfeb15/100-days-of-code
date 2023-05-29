# Day-29

# Password Manager

This is a simple password manager application built with Python's Tkinter library and Pyperclip module. The application generates a random password, saves it, and stores the website, email, and password credentials in a text file.

## Features

* Generate a strong password using letters, numbers, and symbols.
* Save website, email, and password credentials.
* Automatically copy the generated password to the clipboard.
* Error message if any fields are left empty before saving.
* Confirmation message before saving.
* Password Generation: Randomly generates strong passwords consisting of letters, numbers, and symbols.
* Password Storage: Saves website, email, and password information to a JSON file.
* Password Search: Allows users to search for saved passwords based on the website name.

## Requirements

- Python 3.x
- Tkinter library
- pyperclip library

## Installation

1. Clone the repository or download the code.
2. Install the required dependencies by running the following command in your terminal:
   ```
   pip install pyperclip
   ```
3. Run the code using the following command:
   ```
   python password_manager.py
   ```
   
## Usage

1. Run the application: `python password_manager.py`
2. The application window will open.
3. To generate a password:
   - Click on the "Generate Password" button. A strong password will be generated and displayed in the password entry field.
   - Click on the "Copy Password" button to copy the generated password to the clipboard.
4. To save a password:
   - Enter the website name, email/username, and password in the respective fields.
   - Click on the "Add" button to save the information.
   - A confirmation dialog will appear. Click "OK" to save or "Cancel" to cancel the operation.
5. To search for a saved password:
   - Enter the website name in the website entry field.
   - Click on the "Search" button.
   - If a password is found for the entered website, a dialog box will display the associated email/username and password.
6. Close the application window when finished.

## Contributions

Contributions are welcome! If you find any bugs or have any suggestions for improvement, please feel free to create a pull request or open an issue.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).