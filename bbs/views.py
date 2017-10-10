from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from bbs import models
# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


def login_acc(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        passWord = request.POST.get('passWord')
        user = authenticate(username=userName,password=passWord)
        print('user:',user)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            erro = '用户名或密码错误'
            return render(request,'login.html',context={'erro':erro})
    return render(request,'login.html')

def register_acc(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        passWord = request.POST.get('passWord')
        name = request.POST.get('myname')
        if User.objects.filter(username = userName):
            erro = '用户名已存在'
            return render(request,'register.html',context={'erro':erro})
        else:
            user = User.objects.create_user(username=userName,password=passWord)
            user.save()
            userProfile = models.UserProfile()
            userProfile.user = user
            userProfile.userName = name
            userProfile.save()
            login(request,user)
            return render(request,'index.html')
    return render(request,'register.html')

def logout_acc(request):
    logout(request)
    return HttpResponseRedirect('login_acc')