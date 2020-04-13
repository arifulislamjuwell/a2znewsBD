from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import requests
import pprint
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class ProthomAloApiView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        lis=[]
        URL = 'https://www.prothomalo.com/'
        page = requests.get(URL, verify=False)
        if page.status_code == requests.codes.ok:
            print('ho')
            soup = BeautifulSoup(page.content, 'html.parser')
            mydivs = soup.find("a")
            print(mydivs)
        return render(request, 'test.html',{'api': lis})
