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

class ProthomAloApiView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        requests.packages.urllib3.disable_warnings() 

        lis=[]
        URL = 'https://www.prothomalo.com/archive'
        page = requests.get(URL, verify=False)
        if page.status_code == requests.codes.ok:
            soup = BeautifulSoup(page.content, 'lxml')
            tagdiv= soup.find_all('h2' ,class_= "title_holder") 
            for i in tagdiv:
                lis.append(i.find('span', 'title').get_text())
        return JsonResponse({'news': lis})

