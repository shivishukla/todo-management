from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, default=2)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return "{}".format(self.email)
