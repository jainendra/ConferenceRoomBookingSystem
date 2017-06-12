from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class BaseModel(models.Model):
    """
    This is an abstract model to be used by all the other models.
    This provides 2 important timestamp fields - Created and Modified
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.__setitem__('is_superuser', True)
        extra_fields.__setitem__('is_staff', True)
        return self._create_user( email, password, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    This stores all details about a user
    """
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Admin(BaseModel):
    """
    This stores list of Users with admin privileges
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='admin'
    )


class Room(BaseModel):
    """
    This stores details of conference rooms available
    """
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        help_text='Enter the name of the room'
    )
    capacity = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text='Enter the number of person\'s the room can accommodate'
    )


class Booking(BaseModel):
    """
    This stores details of bookings of the conference rooms
    """
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField(
        null=False,
        blank=False,
        help_text='Enter the booking start time'
    )
    end_time = models.DateTimeField(
        null=False,
        blank=False,
        help_text='Enter the booking end time'
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False
    )
