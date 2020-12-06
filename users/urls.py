# _*_ encoding:utf-8 _*_
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
]