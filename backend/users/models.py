from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom User model."""

    class Roles(models.TextChoices):
        """Custom roles for use custom permissions in api"""

        ADMIN = 'admin', _('Administrator')
        USER = 'user', _('User')

    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        _('role'), choices=Roles.choices, default=Roles.USER, max_length=30
    )
    username = models.CharField(
        _('username'),
        unique=True,
        max_length=150,
        validators=[RegexValidator(regex=r'^[\w.@+-]+\Z')],
        error_messages={
            "unique": _('A user with that username already exists.'),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, unique=True)
    last_name = models.CharField(_('last name'), max_length=150, unique=True)

    class Meta:
        ordering = ('username',)
