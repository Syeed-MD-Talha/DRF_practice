from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('api/login',obtain_auth_token,name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/register',RegisterView.as_view(),name='auth_register'),
]

