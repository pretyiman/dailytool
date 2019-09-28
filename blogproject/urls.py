"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path, re_path
from blog import views
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls import handler404


my_app = 'blog'

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('',views.home_page, name ='homepage'),
    path('home',views.welcome, name ='welcome'),
    path('accounts/profile/',views.welcome, name ='welcome'),
    path('inventory/',views.inventory, name ='inventory'),
    path('dailyfinance/',views.dailyfinance, name ='dailyfinance'),

    # path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    path('rackform/',views.rackcreateview.as_view(), name='rack-form'),
    path('racklist/',views.racklistview.as_view(), name='rack-list'),
    path('rackupdate/<int:pk>/',views.rackupdateview.as_view(), name='rack-update'),
    path('rackdelete/<int:pk>/',views.rackdeleteview.as_view(), name='rack-delete'),

    path('warehouseform/',views.warehousecreateview.as_view(),name='warehouse-form'),
    path('warehouselist/',views.warehouselistview.as_view(), name='warehouse-list'),
    path('warehouseupdate/<int:pk>/',views.warehouseupdateview.as_view(), name='warehouse-update'),
    path('warehousedelete/<int:pk>/',views.warehousedeleteview.as_view(), name='warehouse-delete'),

    path('itemform/',views.itemcreateview.as_view(),name='item-form'),
    path('itemlist/<int:pk>/',views.itemdetailview.as_view(), name='item-deatil'),
    path('itemlist/',views.itemlistview.as_view(), name='item-list'),
    path('itemupdate/<int:pk>/',views.itemupdateview.as_view(), name='item-update'),
    path('itemdelete/<int:pk>/',views.itemdeleteview.as_view(), name='item-delete'),

    path('catagoryform/',views.CatagoryFormview.as_view(),name='catagory-form'),
    path('catagorylist/',views.CatagoryListView.as_view(), name='catagory-list'),
    path('catagoryupdate/<int:pk>/',views.CatagoryUpdateView.as_view(), name='catagory-update'),
    path('catagorydelete/<int:pk>/',views.CatagoryDeleteView.as_view(), name='catagory-delete'),

    path('subcatagoryform/',views.SubCatagoryFormview.as_view(),name='subcatagory-form'),
    path('subcatagorylist/',views.SubCatagoryListView.as_view(), name='subcatagory-list'),
    path('subcatagoryupdate/<int:pk>/',views.SubCatagoryUpdateView.as_view(), name='subcatagory-update'),
    path('subcatagorydelete/<int:pk>/',views.SubCatagoryDeleteView.as_view(), name='subcatagory-delete'),


    path('addexpenses/', views.Expensesforminput),
    path('expnesesreport',views.CDR_expenses),
    path('todayexpensesreport', views.DailyExpReport),
    path('yesterdayexpensesreport', views.yesterdayExp),
    path('last7daysexpensesreport', views.LSD_expenses),
    path('last30daysexpensesreport', views.LTD_expenses),
    path('editexpenses/<int:exp_id>/', views.expedit),
    path('expensesupdate/<int:exp_id>', views.expupdate),
    path('deleteexpenses/<int:exp_id>/', views.expdelete),

    path('addincome/', views.incomeforminput),
    path('incomeport',views.CDR_income),
    path('incomerepoting', views.CDR_income),
    path('todaysincomereport', views.DailyincomeReport),
    path('yesterdayincomereport', views.yesterdayincomeReport),
    path('last7daysincomereport', views.LSDincomeReport),
    path('last30daysincomereport', views.LTDincomeReport),
    # path('editincome/<int:income_id>/', views.incomeedit), #first
    path('editincome/<int:income_id>/', views.incomeeditform),
    path('incomeupdate/<int:income_id>', views.incomeupdate),
    path('deleteincome/<int:income_id>/', views.incomedelete),


    path('addcontact/', views.ContacFormEntry),
    path('contactlist/', views.contactlist),
    path('editcontact/<int:contact_ID>/', views.editContact),
    path('contactupdate/<int:contact_ID>', views.contactupdate, name='contact-update'),
    # path('subcatagoryupdate/<int:pk>/',views.SubCatagoryUpdateView.as_view(), name='subcatagory-update'),
    path('deletecontact/<int:contact_ID>/', views.deletecontact),

    path('todo/', views.todo),
    path('deletetodo/<int:list_id>/', views.deletetodo),
    path('crossoff/<int:list_id>/', views.cross_off),
    path('uncross/<int:list_id>/', views.uncross),

    path('search/', views.searchview),
    # path('itemsearch/', views.itemsearch),

    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('blog/',include('django.contrib.auth.urls')),
    path('',include('django.contrib.auth.urls')),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    re_path('accounts/login/', TemplateView.as_view(template_name='login.html'), name='login'), #workinng url
    path('logout/', TemplateView.as_view(template_name='logout.html'), name='logout'),

]

handler404 = 'blog.views.error_404_view'
