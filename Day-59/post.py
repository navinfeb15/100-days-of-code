import requests

class Post:
    def __init__(self):
        self.blog_posts = requests.get("https://api.npoint.io/5deaf41b4f8078c817e6").json()