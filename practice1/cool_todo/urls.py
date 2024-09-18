from django.urls import path
from . import views

urlpatterns = [
    path('',views.todos,name='home_page')
]
