from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

response_url = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts_from_response = response_url.json()

post_objects = []
for post in all_posts_from_response:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/')
def get_all_posts():

    return render_template("index.html", all_posts=all_posts_from_response)

if __name__ == "__main__":
    app.run(debug=True)
