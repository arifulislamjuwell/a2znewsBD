from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import requests
import pprint
from bs4 import BeautifulSoup
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging

logger = logging.getLogger('a2znewsBD')

class SamakalApiView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        requests.packages.urllib3.disable_warnings()
        today= datetime.today().strftime('%Y-%m-%d')
        lis=[]
        for i in range(2):
            if i == 0:
                URL = 'https://samakal.com/archive?date={}'.format(today)
            else:
                URL = 'https://samakal.com/archive?date={}&page=1'.format(today)
            page = requests.get(URL, verify=False)
            if page.status_code == requests.codes.ok:
                soup = BeautifulSoup(page.content, 'html.parser')
                taga= soup.find_all('h4' ,class_= "heading archive-news-heading") 
                for i in taga:
                    lis.append(i.get_text()+'------')

        return JsonResponse({'news': lis})

