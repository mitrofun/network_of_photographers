from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    city = models.ForeignKey(
        'geo.City',
        verbose_name=_('City'),
        related_name='users',
        on_delete=models.CASCADE,
        null=True,
    )

    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username


