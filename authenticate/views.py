from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
import logging

logger = logging.getLogger('a2znewsBD')

class AuthenticateView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        return render(request,'auth.html')

    def post(self, request):
        data=  json.loads(request.body.decode('utf-8'))
        username= data['username']
        password= data['password']
        try:
            user_obj= User.objects.get(username=username)
        except Exception as e:
            return JsonResponse({'result': 'user not found'})

        if user_obj.check_password(password):
            user =auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return JsonResponse({'result': 'found'})
        else:
            return JsonResponse({'result': 'password does not match'})

        # return render(request, 'homepage.html')