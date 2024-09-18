from django.urls import path
from . import views

urlpatterns = [
     path('home/',views.HomeView,name='home'),
     path('login/', views.SignInView.as_view(), name='login'),
     path('logout/', views.SignOutView.as_view(), name='logout'),
     path('signup/', views.SignUp.as_view(), name='signup'),
     
]
