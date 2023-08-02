from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext, gettext_lazy as _


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('age'))
