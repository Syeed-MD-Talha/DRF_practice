from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # Include the hello app's URLs
    path('account/',include('user_app.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]