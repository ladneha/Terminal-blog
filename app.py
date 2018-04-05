_author_ = "neha"

from models.post import Post

post = Post("Post1 title", "Post1 content", "Post1 author")
post2 = Post("Post2 title", "Post2 content", "Post2 author")
post3 = Post("Post3 title", "Post3 content", "Post3 author")

print(post.content)
print(post2.content)