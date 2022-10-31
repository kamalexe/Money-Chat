from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:id>', views.index, name="home"),
    path('chat/<str:chat_id>', views.chat, name="chat"),
    path('home/sendmsg', views.sendmsg, name="sendmsg"),
]
