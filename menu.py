from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
        #Ask user for author name
        self.user = input("Enter your author name: ")
        self.user_blog = None
        #Check if they have already got an account
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        #If not prompt them to create one

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False


    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter description for the blog: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog=blog

    def run_menu(self):
        #ask user read or write?
        read_or_write = input("Do you want to read(R) or write(W) blogs? ")
        if read_or_write == 'R':
          #list blogs in the database
          self._list_blogs()
          self._view_blog()
          #allow user to pick one
          #display the blog
        elif read_or_write == 'W':
          #check if user has a blog
          #if they do, prompt to write a post
          self.user_blog.new_post()
          #else prompt to create a new blog
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter blog id: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))