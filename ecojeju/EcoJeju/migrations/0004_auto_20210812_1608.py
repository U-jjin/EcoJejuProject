# Generated by Django 3.2.6 on 2021-08-12 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoJeju', '0003_auto_20210812_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20, verbose_name='유저 이름'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_pwd',
            field=models.CharField(max_length=20, verbose_name='유저 비밀번호'),
        ),
    ]
