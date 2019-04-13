from django.db import models
from django.contrib.auth.models import AbstractUser

# Let's extend the default user model


class UserModel(AbstractUser):

    age = models.PositiveSmallIntegerField(default=18, blank=False)
    country = models.CharField(max_length=2, blank=False)  # ISO Alpha-2 (Two letter country code)

    # Less ambiguity is better, let's make sure we require the email/country

    REQUIRED_FIELDS = ['email', 'country']

    # Define string repr

    def __str__(self):
        return self.username



