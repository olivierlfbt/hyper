def summary(posts):

    total_posts = len(posts)

    total_tasks = sum(
        len(post["todos"])
        for post in posts
    )

    return {
        "posts": total_posts,
        "tasks": total_tasks
    }
