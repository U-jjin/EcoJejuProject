import json

from django.http import HttpResponse
from django.shortcuts import render

from EcoJeju.models import user


def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def dashboard_v2(request):
    context = {
        'section': 'dashboard_v2.html',
    };
    return render(request,'dashboard.html',context)

def dashboard_v3(request):
    context ={
        'section' :'dashboard_v3.html',
    };
    return render(request,'dashboard.html',context)

def register(request):
    return render(request,'register.html')

def registerimpl(request):
    template_name ='register.html'
    id = request.POST['inputid'];
    pwd = request.POST['inputpwd'];
    repwd = request.POST['inputrepwd'];
    name = request.POST['inputname'];

    if id=='' or pwd=='' or repwd==''or name=='':
        context = {'result': '빈칸을 모두 채워주세요'}
    elif user.objects.filter(user_id =id).exists():
        context = {'result': '이미 존재하는 아이디 입니다.'}
    elif pwd != repwd:
        context = {'result': '비밀번호가 일치하지 않습니다.'}
    else:
        user.objects.create(
            user_id= id,
            user_name= name,
            user_pwd= pwd,
        ).save()
        context = {
            "result": "회원가입을 성공하였습니다.",
            "uid": id,
        }
    return HttpResponse(json.dumps(context), content_type="application/json")

def recover(request):
    return render(request,'recover.html')
# def registerimpl(request):
#     id = request.POST['id'];
#     pwd = request.POST['pwd'];
#     name = request.POST['name'];
#
#     user = UserVO(id,pwd,name);
#     udb.insert(user);
#     print(id,pwd, name);
#     context={
#         'section':'registerok.html',
#         'rname' : name,
#     };
#     return render(request, 'base.html',context);
# Create your views here.
