# Generated by Django 2.1 on 2018-09-03 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180904_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'اسلاید', 'verbose_name_plural': 'اسلاید ها'},
        ),
        migrations.RemoveField(
            model_name='slider',
            name='CreateTime',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='LastEditTime',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='PublishTime',
        ),
    ]
