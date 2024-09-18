from django.contrib.auth.models import User
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Infolist(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class Infodetails(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

class ReviewView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer