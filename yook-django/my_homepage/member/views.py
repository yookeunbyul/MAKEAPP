from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import os

# Create your views here.

def main (req):
    return render( req, 'main.html')

def recruit (req):
    return render( req, 'recruit.html' )

def recruit_done (req):
    new_member = User( username = req.POST.get('name'), userbirth = req.POST.get('birthday'), gender = req.POST.get('member_gender'), useremail = req.POST.get('email'), userphone = req.POST.get('phone'), userschool = req.POST.get('school'), userdepartment= req.POST.get('department'), usergrade= req.POST.get('member_grade'), userarea= req.POST.get('member_area'), userurl= req.POST.get('url') )
    new_member.save()
    print("지원성공")
    return render( req, 'recruit_done.html' )

def recruit_check (req):
    return render( req, 'recruit_check.html' )

def ajax_check (req):
    recruit_member = User.objects.filter(username=req.POST.get('name_'), userphone=req.POST.get('phone_'))

    if recruit_member:
        print("성공")
        return render( req, 'check_sucess.html', {'parameter1': req.POST.get('name_')} )
    else:
        print("실패")
        messages.error(req, '접수된 내역이 없습니다.')
        return redirect('../yook/main')





def login (req):
    return render ( req, 'a.html' )

def logged (req):
    logged_member = User.objects.filter(userid=req.POST.get('id'), password=req.POST.get('pwd'))

    if logged_member:
        print("로그인 성공")
        req.session['userid'] = req.POST.get('id')
        return render ( req, 'logged.html')
    else:
        print("로그인 실패")
        return redirect('../yook/login')

def check_logged (req):
    if req.session.get('userid'):
        print("로그인 성공")
        return render ( req, 'logged.html')
    else:
        print("로그인 실패")
        return render ( req, 'login.html')

def logout (req):
    req.session.pop('userid')
    print("세션 삭제")
    return render ( req, 'login.html')

def chgpwd (req):
    return render ( req, 'chgpwd.html' )

def changed (req):
    change_member = User.objects.get(userid=req.POST.get('id'), password=req.POST.get('pwd'))
    change_member.password = req.POST.get('re_pwd')
    change_member.save()

    if change_member :
        print("변경 성공")
        return render( req, 'login.html' )
    else :
        print("변경 실패")
        return render( req, 'login.html' )

def join (req):
    return render ( req, 'join.html' )

def joined (req):
    new_member = User( username = req.POST.get('name'), userid = req.POST.get('id'), password = req.POST.get('pwd') )
    new_member.save()
    print("회원가입 성공")
    return render ( req, 'login.html')

def delid (req):
    return render ( req, 'delid.html')

def deleted (req):
    delete_member = User.objects.get(userid=req.POST.get('id'), password=req.POST.get('pwd'))
    delete_member.delete()

    if delete_member :
        print("삭제 성공")
        return render( req, 'login.html' )
    else :
        print("삭제 실패")
        return render( req, 'login.html' )

def upload_file(req):
    if req.method == 'POST':
        with open( os.path.abspath( './member/static/' + req.FILES['my_file'].name ), 'wb+' ) as dest:
            for chunk in req.FILES['my_file'].chunks():
                dest.write(chunk)
            return render(req, 'a.html')
    else:
        return render(req, 'upload.html')

def checkbox(req):
    return render( req, 'checkbox.html')

def checkbox_result(req):
    print(req.POST.getlist("my_id"))
    return render( req, 'checkbox_result.html', { 'checkbox' : req.POST.getlist('my_id') } )


