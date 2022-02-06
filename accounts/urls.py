from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token), #accounts/api-token-auth 호출하면 token응답을 받을 수 잇다.
]