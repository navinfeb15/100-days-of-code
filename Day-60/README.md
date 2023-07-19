# Day-60


# Flask Blog

This is a simple Flask application that serves a blog website. Users can view blog posts, navigate through different pages, and contact the website owner using a contact form.

## Installation

1.  Clone the repository:
    ```
    git clone <repository_url>
    
    ```
    
2.  Install the required dependencies. It is recommended to use a virtual environment.
    ```
    pip install -r requirements.txt
    
    ```
    

## Usage

1.  Run the Flask application:
    ```
    python app.py
    ```
    
2.  Open your web browser and visit  [http://localhost:5001](http://localhost:5001/)  to access the blog website.
    

## Routes

The application has the following routes:

-   `/`  - Home page displaying all the blog posts.
-   `/about`  - About page providing information about the website.
-   `/contact`  - Contact page with a form to send a message to the website owner.
-   `/post/<int:index>`  - Individual blog post page with details about a specific post.

## Configuration

-   Modify the  `posts`  variable in the  `app.py`  file to use your own data source for blog posts. Currently, it fetches data from an npoint API.
-   Update the  `my_email`,  `password`, and  `to_email`  variables in the  `app.py`  file with your own email details for the contact form to work properly.

## License

This project is licensed under Free [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.