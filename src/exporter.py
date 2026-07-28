import json

def export(posts):

    with open(
        "data/exports/posts.json",
        "w",
        encoding="utf8"
    ) as f:

        json.dump(posts, f, indent=4)
