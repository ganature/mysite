# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from auto.models import Cases, Modules, TestUsers


# Register your models here.
"""
class TestUsers_Admin (admin.ModelAdmin):
    list_display = ('username', 'creatdata', 'lastmodif')
    search_fields = ('username',)
    ordering = ('creatdata',)


class TestUsers_line (admin.TabularInline):
    model = TestUsers


class Cases_line (admin.TabularInline):
    '''
    
    '''
    model = Cases


class Modules_Admin (admin.ModelAdmin):
    list_display = ('modulesname', 'promodules', 'creatdata', 'lastmodif', 'remark')
    search_fields = ('modulesname',)
    ordering = ('creatdata',)
    inlines = [TestUsers_line]
    #inlines = [Cases_line]


admin.site.register (TestUsers, TestUsers_Admin)
admin.site.register (Modules, Modules_Admin)
admin.site.register (Cases)
"""