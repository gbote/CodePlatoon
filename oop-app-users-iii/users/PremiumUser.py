from users.User import UserInfo

class PremiumUser(UserInfo):

    def __init__(self, first_name, last_name, username, password, address):
        super().__init__(first_name, last_name, username, password, address)