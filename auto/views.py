# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from auto.models import TestUsers,Modules,Cases

# Create your views here.
def index(request):
    return render(request,'index.html')

def test(request):
    modules=Modules.objects.all()
    return render(request,'modules.html',{'modules':modules})

def case(request):	
	cases=Cases.objects.all().select_related('mname')
	return render(request,'testcase.html',{'cases':cases})