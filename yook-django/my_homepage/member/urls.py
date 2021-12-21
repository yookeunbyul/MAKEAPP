from django.urls import path
from . import views

urlpatterns = [
        path('main', views.main),
        path('login', views.login),
        path('logged', views.logged),
        path('check_logged', views.check_logged),
        path('logout', views.logout),
        path('chgpwd', views.chgpwd),
        path('changed', views.changed),
        path('joined', views.joined),
        path('join', views.join),
        path('delid', views.delid),
        path('deleted', views.deleted),
        path('upload', views.upload_file),
        path('checkbox', views.checkbox),
        path('checkbox_result', views.checkbox_result),
        path('recruit', views.recruit),
        path('recruit_done', views.recruit_done),
        path('recruit_check', views.recruit_check),
        path('ajax_check', views.ajax_check)
]
