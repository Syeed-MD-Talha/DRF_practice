

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import IsOwnerOrReadOnly




class hello_world(APIView):
    def get(self,request):
        book=Book.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successfully created.Now refresh your page'})
        return Response(serializer.errors)
    
    
    
class author_form(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    


class ReviewView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewEditView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsOwnerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
class BookListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
