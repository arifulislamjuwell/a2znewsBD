from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

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
        print(username, password)
        return JsonResponse({'user':4234})
        # return render(request, 'homepage.html')