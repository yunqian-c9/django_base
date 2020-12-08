# _*_ encoding:utf-8 _*_
from django.urls import path
from . import views


urlpatterns = [
    path('register/id-<int:id>', views.RegisterView.as_view()),
]