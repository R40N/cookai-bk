from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, nickname, email, password=None):
        if not nickname:
            raise ValueError('닉네임은 필수입니다.')
        if not email:
            raise ValueError('이메일은 필수입니다.')
        
        user = self.model(
            nickname = nickname,
            email = self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, nickname, email, password):
        user = self.create_user(
            nickname = nickname,
            email = self.normalize_email(email),
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']
    
    def __str__(self):
        return self.nickname
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
