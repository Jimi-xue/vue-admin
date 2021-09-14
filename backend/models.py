from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Host(models.Model):
    hostname = models.CharField(u"主机名",max_length=64,null=False, blank=False)
    ip_addr = models.CharField(u"ip",max_length=64,unique=True,null=False, blank=False)
    add_time = models.DateTimeField(u"添加时间",auto_now_add=True)
    asset_id = models.CharField(u"资产id",max_length=50,null=True, blank=True)
    remark = models.CharField(u"备注",max_length=50,null=True, blank=True)

    def __unicode__(self):
        return self.hostname