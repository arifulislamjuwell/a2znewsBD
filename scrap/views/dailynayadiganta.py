from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import requests
import pprint
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging

logger = logging.getLogger('a2znewsBD')

class DailyNayadigantaApiView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        requests.packages.urllib3.disable_warnings() 

        lis=[]
        URL = 'https://www.dailynayadiganta.com/archive'
        page = requests.get(URL, verify=False)
        if page.status_code == requests.codes.ok:
            soup = BeautifulSoup(page.content, 'lxml')
            divh1= soup.find_all('h1', class_="title", limit=20)
            for i in divh1:
                lis.append(i.string.strip()+'------')

        return JsonResponse({'news': lis})
