from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    #LANDING PAGE
    path('landing_page', views.reg_login, name='landing_page'),
    # HOME
    path('',views.home,name='home'),
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