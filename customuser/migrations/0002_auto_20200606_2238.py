# Generated by Django 2.2.10 on 2020-06-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_day',
            field=models.DateField(null=True, verbose_name='誕生日'),
        ),
    ]
