## Day-69

# Flask Blog Application

This is a Flask-based blog application that allows users to register, log in, create blog posts, view and comment on posts, and perform other related actions.

## Features

-   User registration: Users can create an account by providing their email, password, and name. The passwords are securely hashed and stored in the database.
-   User login: Registered users can log in using their email and password.
-   User authentication: User authentication is implemented using Flask-Login, which provides session management and user authentication features.
-   Blog posts: Users can create new blog posts by providing a title, subtitle, body content, and an optional image URL. The posts are stored in the database and displayed on the home page.
-   Post details: Users can view the details of a specific blog post, including the title, subtitle, body content, comments, and author information.
-   Comments: Registered users can leave comments on blog posts. Comments are associated with the corresponding blog post and the user who posted the comment.
-   User profile: Each user has a profile page that displays their name, email, and gravatar image.
-   Edit and delete posts: Users can edit and delete their own posts. Only the author of a post can perform these actions.
-   Access control: Certain routes and actions are restricted to authenticated users or specific user roles.
-   Responsive design: The application is built using Bootstrap 5, providing a mobile-friendly and responsive layout.

## Installation

1.  Clone the repository:  `git clone https://github.com/your-username/flask-blog.git`
2.  Change to the project directory:  `cd flask-blog`
3.  Create a virtual environment (optional):  `python3 -m venv venv`
4.  Activate the virtual environment (optional):
    -   For Linux/Mac:  `source venv/bin/activate`
    -   For Windows:  `venv\Scripts\activate`
5.  Install the required packages:  `pip install -r requirements.txt`
6.  Set the environment variables:
    -   Linux/Mac:  `export FLASK_APP=app.py`
    -   Windows (PowerShell):  `$env:FLASK_APP = "app.py"`
7.  Run the application:  `flask run`

Note: Make sure you have Python and pip installed on your system.

## Usage

-   Open your web browser and visit  `http://localhost:5000`  to access the application.
-   Register a new account by providing your email, password, and name.
-   Log in with your registered email and password.
-   Create new blog posts, view existing posts, and interact with the application.
-   Enjoy blogging!

## Contributing

Contributions are welcome! If you find any issues or want to enhance the application, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

