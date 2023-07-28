## Day-67


# Flask Blog

Flask Blog is a web application that allows users to create, edit, and delete blog posts. It provides a user-friendly interface for managing a blog and is built using the Flask framework.

## Features

-   Displaying all blog posts on the homepage
-   Viewing individual blog posts
-   Creating new blog posts
-   Editing existing blog posts
-   Deleting blog posts
-   Form validation for creating and editing posts
-   Integration with CKEditor for rich text editing

## Installation

1.  Clone the repository:  `git clone https://github.com/your-username/flask-blog.git`
2.  Navigate to the project directory:  `cd flask-blog`
3.  Create a virtual environment:  `python3 -m venv venv`
4.  Activate the virtual environment:
    -   For Windows:  `venv\Scripts\activate`
    -   For macOS/Linux:  `source venv/bin/activate`
5.  Install the required dependencies:  `pip install -r requirements.txt`
6.  Run the application:  `python app.py`
7.  Open your web browser and visit  `http://localhost:5003`  to access the Flask Blog application.

## Usage

-   To view all blog posts, go to the homepage (`http://localhost:5003`).
-   To view a specific blog post, click on its title or navigate to  `/post_id`, where  `post_id`  is the ID of the post.
-   To create a new blog post, click on the "New Post" button on the homepage and fill out the required fields in the form.
-   To edit an existing blog post, click on the "Edit" button next to the post on the homepage or the post's page.
-   To delete a blog post, click on the "Delete" button next to the post on the homepage or the post's page.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


## License

This project is licensed under Free [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.

## Acknowledgements

-   This project was inspired by the Flask Mega-Tutorial by Miguel Grinberg.
-   The Flask framework:  [Flask](https://flask.palletsprojects.com/)
-   Flask-WTF:  [Flask-WTF](https://flask-wtf.readthedocs.io/)
-   Flask-CKEditor:  [Flask-CKEditor](https://flask-ckeditor.readthedocs.io/)
-   SQLAlchemy:  [SQLAlchemy](https://www.sqlalchemy.org/)
