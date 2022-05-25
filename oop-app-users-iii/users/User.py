class UserInfo:

    all_posts = []


    def __init__(self, first_name, last_name, username, password, address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.address = address
        self.all_posts = []

    def user_post(self):
        self.post = input("Type your post: ")
        self.all_posts.append(self.post)
        UserInfo.all_posts.append(f"{self.username} posted {self.post}")

    def show_user_posts(self):
        return f'{self.username} posts: {self.all_posts}'

    @classmethod
    def show_all_posts(cls):
        for post in cls.all_posts:
            print(post)
            print('-----------')