_author_ = "neha"

from models.post import Post
from database import Database
from models.blog import Blog

Database.initialize()

blog = Blog(author="Neha",
            title="Sample title",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
#post.save_to_mongo()

#print(post2.content)