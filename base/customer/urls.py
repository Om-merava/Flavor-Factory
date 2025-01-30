from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/',views.home,name='home')
    # You can add more URL patterns as needed, such as a home page
]
