from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path('',views.home,name='home'),
    path('reg_login', views.reg_login, name='reg_login'),
    

]