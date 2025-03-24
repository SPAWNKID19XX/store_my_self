from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email) 
        is_customer = extra_fields.pop('is_customer', True)
        user = self.model(email=email, **extra_fields) 
        user.set_password(password) 
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class CustomUser(AbstractUser):
    """
    An abstract CustomUser class implementing a fully featured User model with
    admin-compliant permissions.

    Username, email and password are required. Other fields are optional.
    """
    is_customer = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    object = UserManager()

    def __str__(self):
        return self.email
