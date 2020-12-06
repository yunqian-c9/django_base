from django.shortcuts import render
from django.views import View
from django import http

# Create your views here.


class RegisterView(View):

    def get(self, request):

        return http.HttpResponse('注册页面-GET')

    def post(self, request):

        return http.HttpResponse('注册页面-POST')
