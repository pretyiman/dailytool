from django.conf.urls import url
from django.urls import path, re_path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    url('',views.home_page,name='index'),
    path('login/', auth_views.LoginView, {'template_name':'accounts/login.html'}, name='login')

]
