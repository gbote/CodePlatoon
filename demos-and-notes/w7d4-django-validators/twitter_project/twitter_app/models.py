from tkinter import W
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import *

# In general, for simple validators write your own validators b/c its easier to understand - you
# don't have to learn builtin behavior.
#
# But for more complex validators, using builtin validators is good.
# EmailValidator is a great example of this - email validation is surprisingly complicated.

def validate_age(age):
    if age < 13:
         raise ValidationError(f"You need to be 13 years of age or older. You currently are {age} years old.")


def validate_account_type(account_type):
    valid_account_types = ['paid', 'free']
    if account_type not in valid_account_types:
        raise ValidationError(f"{account_type} is not valid. Please select a valid account type {valid_account_types}.")

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    account_type = models.CharField(max_length=4, validators=[validate_account_type])

    # Two ways of doing the same thing
    age = models.IntegerField(validators=[validate_age])
    #age = models.IntegerField(validators=[MinValueValidator(13)])


    
