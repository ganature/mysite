# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import TestUsers,Modules,Cases

# Create your views here.
def index(request):
    return render(request,'index.html')

def test(request):
    module=Modules.modulesname

    return render(request,'index.html')