from src.todo_manager import add_task

def test_task():

    post = {
        "todos": []
    }

    add_task(post, "Write intro")

    assert len(post["todos"]) == 1
