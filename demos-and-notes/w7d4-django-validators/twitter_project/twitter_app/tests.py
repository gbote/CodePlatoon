from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

# Create your tests here.
class AppUserTest(TestCase):

    # Test that age validator is working
    def test_01_create_user_age(self):
        new_user = User(
                first_name='Adam', 
                last_name='Cahan',
                email='adam@codeplatoon.org',
                age=12,
                account_type='free',
            )

        try: 
            new_user.full_clean()
            self.fail() # it should fail here
        except ValidationError as e:
            self.assertTrue('You need to be 13 years of age or older. You currently are 12 years old.' in e.message_dict['age'])


    # # test user account validation failure case
    # def test_01_create_user_account_type(self):
    #     new_user = User(
    #             first_name='Adam', 
    #             last_name='Cahan',
    #             email='adam@codeplatoon.org',
    #             age=14,
    #             account_type='free',
    #         )

    #     try: 
    #         new_user.full_clean()
    #         self.fail() # it should fail here
    #     except ValidationError as e:
    #         self.assertTrue("foo is not valid. Please select a valid account type ['paid', 'free']." in e.message_dict['account_type'])


    # def test_01_create_user_account_type_success(self):
    #     new_user = User(
    #             first_name='Adam', 
    #             last_name='Cahan',
    #             email='adam@codeplatoon.org',
    #             age=14,
    #             account_type='paid',
    #         )

    #     new_user.full_clean()
    #     # save to database & confirm is correct

    #     new_user2 = User(
    #             first_name='Adam', 
    #             last_name='Cahan',
    #             email='adam@codeplatoon.org',
    #             age=14,
    #             account_type='free',
    #         )

    #     new_user2.full_clean()
