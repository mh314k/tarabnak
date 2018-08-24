# Generated by Django 2.1 on 2018-08-24 10:15

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CommentTime', models.DateTimeField(auto_created=True, verbose_name='زمان نظر دادن')),
                ('CommenterName', models.CharField(default='کاربر ناشناس', max_length=200, verbose_name='نام نظردهنده')),
                ('CommentBody', models.TextField(max_length=1000, verbose_name='متن نظر')),
                ('CommenterUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر نظردهنده')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرها',
                'ordering': ['-CommentTime'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-PublishTime'], 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AlterField(
            model_name='post',
            name='Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Posts', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.user_directory_path, verbose_name='تصویر پست'),
        ),
        migrations.AddField(
            model_name='comment',
            name='PostTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='COMMENTS', to='blog.Post', verbose_name='پست مورد نظر'),
        ),
    ]