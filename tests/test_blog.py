from src.validator import valid_title

def test_blog():

    assert valid_title("Python Tips")
