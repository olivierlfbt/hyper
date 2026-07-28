import json
import os

POSTS = "data/posts.json"

def load_posts():

    if not os.path.exists(POSTS):
        return []

    with open(POSTS, encoding="utf8") as f:
        return json.load(f)

def save_posts(posts):

    with open(POSTS, "w", encoding="utf8") as f:
        json.dump(posts, f, indent=4)
