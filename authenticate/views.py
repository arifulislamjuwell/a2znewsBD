from django.shortcuts import render
from django.views import View
# Create your views here.


class AuthenticateView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        return render(request,'auth.html')