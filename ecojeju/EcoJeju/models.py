from django.db import models

class user(models.Model):
    user_id = models.CharField(max_length=20, unique=True, verbose_name="유저 아이디", primary_key=True)
    user_pwd = models.CharField(max_length=20, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=20, verbose_name= '유저 이름')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="계정생성시간")

    def __str__(self):
        return self.name;
    class Meta:
        db_table = 'user'
        verbose_name ='개인 사용자 유저'
        verbose_name_plural='개인 사용자 유저'

