from src.search import by_title

def test_search():

    posts = [
        {"title": "Learning Python"}
    ]

    assert len(by_title(posts, "Python")) == 1
