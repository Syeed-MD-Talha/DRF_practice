from django.urls import path
from . import views

urlpatterns = [
    path('',views.Infolist.as_view(), name='InfoList'),
    path('<int:pk>',views.Infodetails.as_view(), name='InfoDetails'),
    path('<int:pk>/review',views.ReviewView.as_view(), name='Review'),
]
