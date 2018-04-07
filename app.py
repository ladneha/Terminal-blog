_author_ = "neha"

from models.post import Post
from database import Database
from models.blog import Blog
from menu import Menu

Database.initialize()

menu = Menu()
menu.run_menu()
