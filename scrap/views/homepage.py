from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
import logging

logger = logging.getLogger('a2znewsBD')

class HomePageView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'homepage.html')