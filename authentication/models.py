from django.db import models
from django.contrib.auth.models import (PermissionsMixin, AbstractBaseUser)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from rest_framework_simplejwt.tokens import RefreshToken

from manager.models import MyUserManager



class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True, blank=False, 
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), max_length=150, unique=True, blank=False)
    is_vendor = models.BooleanField(
        _('vendor status'),
        default=False,
        help_text=_('Designates whether the user is Vendor status.'),
    )
    is_client = models.BooleanField(
        _('client status'),
        default=False,
        help_text=_('Designates whether the user is Client status.'),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    email_verified=models.BooleanField(
        _('email_verified'),
        default=False,
        help_text=_(
            'Designates whether this user email is verified. '
        ),
    )
    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
