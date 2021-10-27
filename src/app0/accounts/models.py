from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    # only required fields in here
    def create_user(self, email, password, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Email pls..")
        if not password:
            raise ValueError("Password pls..")
        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(self)
        user_obj.staff = is_staff
        user_obj.admim = is_admin
        user_obj.active = is_active

        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        # if not email:
        #     raise ValueError("Email for staff pls..")
        user = self.create_user(
            email, password=password, is_staff=True
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        # if not email:
        #     raise ValueError("Email for staff pls..")
        user = self.create_user(
            email, password=password, is_staff=True, is_admin=True
        )
        user.save(using=self._db)
        return user

# ----------------- CUSTOM USER MODEL--------------------


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email ID",
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    # notice the absence of a "Password field", that is built in.

    # username = models.CharField(max_length=20, unique=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=20)

    USERNAME_FIELD = "email"  # suername
    # USERNAME_FIELD & password are req.
    REQUIRED_FIELD = []  # ['first_name'] - user related other data can be in Profile app

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    # def set_password(self):
    #     return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        # "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        # "Is the user account active?"
        return self.active
