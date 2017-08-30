# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class TestUsers(models.Model):
    username=models.CharField(max_length=20,verbose_name=u'用户名')
    password=models.CharField(max_length=20,verbose_name=u'密码')
    creatdata=models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    lastmodif=models.DateField(auto_now=True,verbose_name=u'最后修改时间')
    def __unicode__(self):
        return self.username

class Modules(models.Model):
    modulesname=models.CharField(max_length=50,verbose_name=u'模块名称')
    promodules=models.ForeignKey('self')
    creatdata=models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    lastmodif=models.DateField(auto_now=True,verbose_name=u'最后修改时间')
    author=models.ForeignKey(TestUsers)
    remark=models.CharField(max_length=50,verbose_name=u'备注')
    def __unicode__(self):
        return self.modulesname
        
class Cases(models.Model):
    mname=models.ForeignKey(Modules,on_delete=models.CASCADE)
    casename=models.CharField(max_length=50,verbose_name=u'用例名称')
    creatdata=models.DateField(auto_now_add=True,verbose_name=u'创建时间')
    lastmodif=models.DateField(auto_now=True,verbose_name=u'最后修改时间')
    remark=models.CharField(max_length=50,verbose_name=u'备注')
    def __unicode__(self):
        return self.casename
    