from django.contrib import admin
from django.urls import path
from jagdambaapp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('reg', views.reg,name='reg'),
]
