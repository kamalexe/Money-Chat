from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:id>', views.index, name="home"),
    path('home/sendmsg', views.sendmsg, name="sendmsg"),
]
