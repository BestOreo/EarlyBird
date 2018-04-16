#coding:utf-8
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .models import User
from django.http import JsonResponse

# Create your views here.

#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())

def homepage(req):
    return render_to_response('homepage.html',{})

def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            #User.objects.get_or_create(username = username,password = password)
            registAdd = User.objects.get_or_create(username = username,password = password)[1]
            if registAdd == False:
                #return HttpResponseRedirect('/share/')
                return render_to_response('share.html',{'registAdd':registAdd,'username':username})
            else:
                return render_to_response('share.html',{'registAdd':registAdd})

    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(req))

def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #对比提交的数据与数据库中的数据
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/index/')
                #将username写入浏览器cookie，失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    A ='ABC'
    return render_to_response('login.html',{'uf':uf,'A':A},context_instance=RequestContext(req))


#登录成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username})

#退出登录

def logout(req):
    response = HttpResponse('logout!!!')
    #清除cookie里保存的username
    response.delete_cookie('username')
    return response


def share(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            return render_to_response('share.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('share.html',{'uf':uf})

a = [1,2,3,4,5]
def ajax_list(request):
    username = request.COOKIES.get('username', '')
    print(username)
    if request.session.get(username) == None:
        request.session[username] = 0
        return JsonResponse([a[0]], safe=False)
    else:
        request.session[username] += 1
        i = request.session[username]
        return JsonResponse([a[i%5]], safe=False)
