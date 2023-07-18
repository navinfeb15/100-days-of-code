# Day-59

# Flask Blog

This is a simple Flask application that displays blog posts. It uses the Flask framework and renders HTML templates to display the content.

## Installation

To run this application, you need to have Python installed on your system. You can download Python from the official website: [Python.org ↗](https://www.python.org/).

1. Clone the repository:

   ````shell
   git clone https://github.com/navinfeb15/100-days-of-code.git
   ```

   ````

1. Navigate to the project directory:

   ````shell
   cd flask-blog
   ```

   ````

1. Install the required dependencies:

   ````shell
   pip install -r requirements.txt
   ```

   ````

## Usage

To start the Flask application, run the following command:

```shell
python app.py
```

The application will be accessible at [http://localhost:5000/ ↗](http://localhost:5000/).

### Home Page

The home page displays a list of blog posts. Each post includes a title and a brief description. Clicking on a post will take you to the individual post page.

### Individual Post Page

The individual post page displays the full content of a specific blog post. You can navigate to different posts by changing the `num` parameter in the URL. For example, to view the second post, go to [http://localhost:5000/post/2 ↗](http://localhost:5000/post/2).

## Customization

You can customize the blog posts by modifying the `blog_posts` list in the `post.py` file. Each post is represented by an instance of the `Post` class, which has `title` and `content` attributes.

```python
# post.py

class Post:
    def __init__(self):
        self.blog_posts = [
            {
                'title': 'First Post',
                'content': 'This is the content of the first post.'
            },
            {
                'title': 'Second Post',
                'content': 'This is the content of the second post.'
            },
            # Add more posts here
        ]
```

Feel free to add more posts or modify the existing ones to suit your needs.

## License

This project is licensed under Free [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.