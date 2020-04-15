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

class BdProtidinView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        requests.packages.urllib3.disable_warnings() 
        lis=[]
        URL = 'https://www.bd-pratidin.com/'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(URL, verify=False, headers=headers)

        if page.status_code == requests.codes.ok:
            soup = BeautifulSoup(page.content, 'lxml')
            tagdiv= soup.find_all('div', class_='home-latest-news')
            tagli= tagdiv[0].find_all('span', limit=20)
            for i in tagli:
                lis.append(i.get_text()+'------')
        return JsonResponse({'news': lis})