from django.urls import path
from .views.prothom_alo import ProthomAloApiView
app_name="scrap"

urlpatterns = [
    path('prothom-alo/',ProthomAloApiView.as_view(), name='prothom_alo'),

]
