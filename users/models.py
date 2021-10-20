import os
from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.name, instance.identity_card, ext)
    return os.path.join(instance.major.name, filename)  # 系统路径分隔符差异，增强代码重用性

class User(AbstractUser):
    phone = models.CharField(u"手机号码",max_length=11)
    avatar =  models.ImageField('个人头像', upload_to = user_directory_path, blank = True, null = True)
    introduction = models.TextField(u"个人介绍",null=True,blank=True)

    def photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return '/api/media/default/user.jpg'
