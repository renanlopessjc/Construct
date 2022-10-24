from unittest.util import _MAX_LENGTH

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Users (AbstractUser):
    choices_cargo = (('V','Vendedor'),
                    ('G','Gerente'))
    cargo = models.CharField(max_length=1, choices = choices_cargo)

