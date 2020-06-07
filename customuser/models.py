from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'
    address = models.CharField(verbose_name='住所', blank=False, max_length=100) 
    birth_day = models.DateField(verbose_name='誕生日', blank=False, null=True)
