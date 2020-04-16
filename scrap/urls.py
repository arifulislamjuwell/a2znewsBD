from django.urls import path
from .views.prothom_alo import ProthomAloApiView
from .views.bd_protidin import BdProtidinView
from.views.samakal import SamakalApiView
from.views.dailynayadiganta import DailyNayadigantaApiView
from.views.homepage import HomePageView

app_name="scrap"

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('prothom-alo/',ProthomAloApiView.as_view(), name='prothom_alo'),
    path('bd-protidin/',BdProtidinView.as_view(), name='bd-protidin'),
    path('samakal/',SamakalApiView.as_view(), name='samakal'),
    path('dailynayadiganta/',DailyNayadigantaApiView.as_view(), name='dailynayadiganta'),

]
