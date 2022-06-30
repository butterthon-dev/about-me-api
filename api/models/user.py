from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from api.models.base import BaseModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email, and password.

        Args:
            email : str
                メールアドレス
            password : str
                パスワード
            extra_fields : Dict[str, Any]
                オプション

        Returns:
            作成したユーザーモデル
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(max_length=150, blank=True, verbose_name='姓')
    first_name = models.CharField(max_length=150, blank=True, verbose_name='名')
    email = models.EmailField(blank=True, unique=True, verbose_name='メールアドレス')
    is_staff = models.BooleanField(default=True, verbose_name='スタッフフラグ')
    is_active = models.BooleanField(default=True, verbose_name='有効フラグ')

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'blog_users'
        verbose_name = verbose_name_plural = 'ユーザー'
