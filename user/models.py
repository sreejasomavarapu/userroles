from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin =models.BooleanField('Is Admin',default=False)
    is_volunteer =models.BooleanField('Is Volunteer',default=False)
    is_coordinator =models.BooleanField('Is Coordinator',default=False)
