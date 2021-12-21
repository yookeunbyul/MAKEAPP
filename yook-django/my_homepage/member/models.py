from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField()

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='이름')
    userbirth = models.DateField(null=True, blank=True, verbose_name='생년월일')
    GENDERS = ( ('M','남성(Man)'),('W','여성(Woman)'),('Q','선택안함') )
    gender=models.CharField(max_length=1, verbose_name='성별', choices=GENDERS, null=True, default='')
    useremail = models.EmailField(max_length=128, verbose_name='이메일')
    userphone = models.TextField(max_length=128, verbose_name='전화번호', null=True, blank=True)
    userschool = models.CharField(max_length=128, verbose_name='학교', null=True, blank=True)
    userdepartment = models.CharField(max_length=128, verbose_name='학과', null=True, blank=True)
    GRADES = ( ('1','1학년'),('2','2학년'),('3','3학년'),('4','4학년') )
    usergrade = models.CharField(max_length=64, verbose_name='학년', choices=GRADES, null=True, default='')
    AREAS = ( ('A','Android 개발자'),('I','iOS 개발자'),('W','Web 개발자'),('S','서버 개발자'),('WD','디자이너 (Web UI/UX)'),('AD','디자이너 (App UI/UX)'),('P','기획자') )
    userarea = models.CharField(max_length=128, verbose_name='지원분야', choices=AREAS, null=True, default='')
    userurl = models.URLField(max_length=200, verbose_name='깃허브/블로그 url', null=True, blank=True)
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록')

    def __str__(self):
        return self.username