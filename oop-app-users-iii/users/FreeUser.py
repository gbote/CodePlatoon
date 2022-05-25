from users.User import UserInfo

class FreeUser(UserInfo):

    def __init__(self, first_name, last_name, username, password, address):
        super().__init__(first_name, last_name, username, password, address)

    def user_post(self):
        if len(self.all_posts) < 2:
            self.post = input("Type your post:")
            self.all_posts.append(self.post)
            super().all_posts.append(f"{self.username} posted {self.post}")
        else:
            print(f'{self.username} You have reached your post limit. Please upgrade your account to continue posting')