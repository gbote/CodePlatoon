from users.FreeUser import FreeUser
from users.User import UserInfo
from users.PremiumUser import PremiumUser

allen = PremiumUser('Allen', 'Smith', 'ASmith452', 'asfkskf', '123 Penny Lane San diego, CA 92011')

jane = FreeUser('Jane', 'Belcher', 'janeB980', 'abcnja', '8566 Blue Ave Orlando, FL 58442')

jane.user_post()
allen.user_post()
jane.user_post()
allen.user_post()
jane.user_post()
allen.user_post()
allen.user_post()


UserInfo.show_all_posts()
print(jane.show_user_posts())
print(allen.show_user_posts())