from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.Author.id, filename)

class Post(models.Model):
    stsChoice = (
        ('P','منتشر شده'),
        ('D','پیشنویس')
    )
    Title = models.CharField(max_length=180,verbose_name='عنوان پست')
    Slug = models.SlugField(unique_for_date="PublishTime",verbose_name='نشانک پست')
    Body = models.TextField(verbose_name='متن پست')
    Author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='AUTHOR',verbose_name='نویسنده پست',null=True)
    PublishTime = models.DateTimeField(verbose_name='تاریخ انتشار')
    CreateTime = models.DateTimeField(auto_now_add=True)
    LastEditTime = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=1, choices=stsChoice, verbose_name='وضعیت انتشار',default='d')
    Tags = TaggableManager(verbose_name='برچسب های پست',help_text='تگ ها را با علامت کاما جدا کنید.',blank=True)
    Image = models.ImageField(verbose_name='تصویر پست',upload_to=user_directory_path,null=True)

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = 'پست ها'
        ordering = ['-PublishTime']

    def __str(self):
        return "{} نوشته شده توسط {} {}({})".format(self.Title,self.Author.first_name, self.Author.last_name,self.Author.username)

