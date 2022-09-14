from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password=None):
        user =  self.model(
            username=username,
            type="manager"
        ) 
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    USER_CHOICES = (
        ("manager", "운영자"),
        ("general", "일반 사용자"),
    )

    username = models.CharField("사용자 아이디", max_length=12, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    type = models.CharField("유저 유형", max_length=100, choices=USER_CHOICES, default="general")
    
    def __str__(self):
        return f"{self.username}"

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin