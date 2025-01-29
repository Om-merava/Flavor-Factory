from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    # HOME
    path('',views.home,name='home'),
    path('reg_login', views.reg_login, name='reg_login'),
    # OFFERS
    path('offers', views.offers, name='offers'),
    # CART
    path('cart', views.cart, name='cart'),
    # MENU
    path('menu', views.menu, name='menu'),
    #PAYMENT
    path('payment', views.payment, name='payment'),
    #ORDER TRACKING
    path('order_tracking', views.order_tracking, name='order_tracking'),




    

]