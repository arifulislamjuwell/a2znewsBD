from django.urls import path
from .views.prothom_alo import ProthomAloApiView
from .views.bd_protidin import BdProtidinView
from.views.homepage import HomePageView

app_name="scrap"

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('prothom-alo/',ProthomAloApiView.as_view(), name='prothom_alo'),
    path('bd-protidin/',BdProtidinView.as_view(), name='prothom_alo'),

]
