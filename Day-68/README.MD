## Day-68



# Flask User Management

This is a Flask application that demonstrates user registration, login, and logout functionality.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [License](#license)

## Description

This Flask application allows users to register, login, and logout. It uses a SQLite database to store user information and provides secure password handling using the `werkzeug.security` module. The application also demonstrates the usage of Flask's `render_template` function to generate HTML templates and the `flask_login` extension for managing user sessions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flask-user-management.git
   ```

2. Change the working directory to the project directory:

   ```bash
   cd flask-user-management
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:

   ```bash
   python app.py
   ```

7. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

- Register: Visit the registration page (`/register`) and provide your email, password, and name to create a new account.
- Login: Visit the login page (`/login`) and enter your email and password to log in to your account.
- Logout: Click the "Logout" link in the navigation bar to log out of your account.
- Secrets: After logging in, you will be redirected to the secrets page (`/secrets`), where you can view user-specific secrets.
- Download: Logged-in users can download a cheat sheet PDF file by visiting the download page (`/download`).

## Routes

- `/`: Home route that displays a welcome message and links to register and login.
- `/register`: Register route for creating a new user account.
- `/login`: Login route for logging in to an existing user account.
- `/secrets`: Secrets route that displays user-specific secrets (requires authentication).
- `/logout`: Logout route for logging out of the current user session.
- `/download`: Download route for downloading a cheat sheet PDF file (requires authentication).

## License

This project is licensed under the [MIT License](LICENSE).


Feel free to customize this `README.md` file further based on your specific project requirements and add more sections if needed.
