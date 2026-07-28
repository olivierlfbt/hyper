def add_task(post, task):

    post["todos"].append({
        "title": task,
        "completed": False
    })
