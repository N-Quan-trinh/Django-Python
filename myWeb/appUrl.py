from django.urls import path
from django.contrib import admin
from myWeb import views
from django.conf.urls import include, url

urlpatterns = [
    path('page1', views.hello_world, name='Hello'),
    path('page2', views.modelTest, name='modelTest'),
    path('register', views.AccountRegister, name='AccountRegister'),
    path('', views.AccountLogin, name='AccountLogin')

]
