
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
            self.user_blog = blog
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
          #allow user to pick one
          #display the blog
        elif read_or_write == 'W':
          #check if user has a blog
          #if they do, prompt to write a post
          #else prompt to create a new blog
        else:
            print("Thank you for blogging!")
