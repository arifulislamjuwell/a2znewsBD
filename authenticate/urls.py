from django.urls import path
from authenticate.views import AuthenticateView

app_name="auth"

urlpatterns = [
    path('authenticate/',AuthenticateView.as_view(), name='authenticate'),
    path('login/', AuthenticateView.as_view(), name= 'login')
]
