from flask import Flask, render_template
from post import Post

app = Flask(__name__)
blog = Post()

@app.route("/")
def home():
    print(blog.blog_posts)
    return render_template("index.html", blog_posts = blog.blog_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", post=blog.blog_posts[num-1])


if __name__ == "__main__":
    app.run(debug=True)