# Django Auth


the default user model is very generic, and probably doesn't meet all of our needs
we'll need to extend it. there are 3 ways to do this:


One option is using a 'profile model' that has a one-to-one relationship with the user model
```python
from django.contrib.auth.models import User

class Employee(models.Model):
    department = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

Another option is to create a subclass of django's built-in `AbstractBaseUser` class. This lets us use django's authentication features, but requires us to define all the fields our user needs.

The third option is to create a subclass of django's built-in `AbstractUser` class. This is a full, functional user model, that we can also extend with custom properties. 