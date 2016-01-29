#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def showHome(request):
    return render(request,'home.html')

def tmpf(request):
    return HttpResponse(u"欢迎光临 自强学堂!")