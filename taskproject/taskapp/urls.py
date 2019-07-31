from django.urls import path
from django.conf.urls import url
from taskapp import views

urlpatterns = [


    path('login/', views.logindetails, name='logindetails'),
    path('welcome/', views.welcomee, name='welcomee'),
    path('logout/', views.user_logout, name='user_logout'),
    path('signup/', views.sign, name='sign'),

    ]
