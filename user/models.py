from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='이름')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자들'
