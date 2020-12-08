import json
from django.shortcuts import render
from django.views import View
from django import http

# Create your views here.


class RegisterView(View):

    def get(self, request, id):

        name = request.GET.get('name', '张三')
        age = request.GET.get('age', 0)

        _id = id

        return http.HttpResponse(f'GET - 参数：name--{name}, age--{age}, id--{_id}')

    def post(self, request, id):

        name = request.POST.get('name', '张三')
        age = request.POST.get('age', 0)

        json_bytes = request.body
        json_data = json.loads(json_bytes)
        print(json_data, type(json_data))

        return http.HttpResponse(f'POST - 参数：name--{name}, age--{age}, json--{json_data}')
