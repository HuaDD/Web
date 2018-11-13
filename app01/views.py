# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
from utils.pagers import Page_Info
from app01 import models
import hashlib
import re


def md5(user,pwd):
    md5_obj = hashlib.md5(user.encode('utf-8'))
    md5_obj.update(pwd.encode('utf-8'))
    encryption = md5_obj.hexdigest()
    return  encryption


def user_info(request):
    user = request.POST.get('username')
    phone = request.POST.get('phone')
    pwd = request.POST.get('password')
    return user,phone,pwd

def register(request):
    """
    
    :param request: 注册
    :return: 
    """

    if request.method == 'POST':
        user,phone,pwd = user_info(request)
        obj = re.match("^(?:(?=.*[a-z])(?=.*[0-9])).*$", pwd)
        if len(pwd) < 16 and obj:
            encryption = md5(user,pwd)
        else:
            return render(request, 'register.html', {'err': '密码格式不对'})
        data = models.User.objects.filter(user=user)
        for i in data:
            if i.user:
                return render(request,'register.html',{'tips':'创建失败，用户已存在'})
        else:
            models.User.objects.create(user=user, phone=phone, password=encryption)
            return redirect('/login/')

    return render(request,'register.html')

def login(request):
    """

    :param request: 登录
    :return: 
    """
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        encryption = md5(user, pwd)
        for value in models.User.objects.filter(user=user):
            if value.user == user and value.password == encryption:
                return redirect('/backstage/')
        else:
            return render(request, 'login.html', {'err': '用户名或密码不对，请重新登录'})

    return render(request, 'login.html')


def backstage(request):
    """

    :param request: 首页
    :return: 
    """
    all_count = models.User.objects.all().count()
    page_info = Page_Info(request.GET.get('page'), all_count, 10, '/backstage/', 11)
    user_list = models.User.objects.all()[page_info.start():page_info.end()]
    if request.method == 'POST':
        serach_value = request.POST.get('search')
        if serach_value.isdigit() and len(serach_value) == 11:
            user_list = models.User.objects.filter(phone=serach_value)
            return render(request,'search.html',{'user_list':user_list})
        elif serach_value.isdigit():
            user_list = models.User.objects.filter(id=serach_value)
            return render(request,'search.html',{'user_list':user_list})
        else:
            user_list = models.User.objects.filter(user=serach_value)
            return render(request,'search.html',{'user_list':user_list})

    return render(request,'backstage.html',{'user_list':user_list,'page_info':page_info})

def create(request):
    """

    :param request: 创建用户
    :return: 
    """

    if request.method == 'POST':
        user, phone, pwd = user_info(request)
        obj = re.match("^(?:(?=.*[a-z])(?=.*[0-9])).*$", pwd)
        if len(pwd) < 16 and obj:
            encryption = md5(user,pwd)
        else:
            return render(request, 'create.html', {'err': '密码格式不对'})
        data = models.User.objects.filter(user=user)
        for i in data:
            if i.user:
                return render(request,'create.html',{'tips':'创建失败，用户已存在'})
        else:
            models.User.objects.create(user=user, phone=phone, password=encryption)
            return redirect('/backstage/')
    return render(request,'create.html')


def delete(request):
    """

    :param request: 删除用户
    :return: 
    """

    if request.method == 'POST':
        del_user = request.POST.get('username')
        models.User.objects.filter(user=del_user).delete()
        return redirect('/backstage/')

    return render(request,'delete.html')



def change_phone(request):
    """

    :param request: 修改手机号
    :return: 
    """
    if request.method == 'POST':
        user = request.POST.get('username')
        old_phone = request.POST.get('old_phone')
        new_phone = request.POST.get('new_phone')
        data = models.User.objects.filter(user=user)
        for i in data:
            if i.phone == int(old_phone):
                user_obj = models.User.objects.get(user=i.user)
                user_obj.phone = new_phone
                user_obj.save()
                return redirect('/backstage/')
    return render(request,'change_phone.html')

def change_pwd(request):
    """

    :param request: 修改密码
    :return: 
    """
    if request.method == 'POST':
        user = request.POST.get('username')
        old_pwd = request.POST.get('old_pwd')
        new_pwd = request.POST.get('new_pwd')
        encryption = md5(user,old_pwd)
        data = models.User.objects.filter(user=user)
        for i in data:
            if i.password == encryption:
                user_obj = models.User.objects.get(user=i.user)
                new_encryption = md5(user, new_pwd)
                user_obj.password = new_encryption
                user_obj.save()
                return redirect('/backstage/')
    return render(request,'change_pwd.html')


