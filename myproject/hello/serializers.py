from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'
        
             
class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(source='user.username',read_only=True)
    book=serializers.CharField(source='book.title',read_only=True)
    class Meta:
        model=Review
        fields='__all__'
    
    def validate(self,data):
        if data['user_rating'] < 1 or data['user_rating'] > 5:
            raise serializers.ValidationError("Rating should be between 1 and 5")
        return data
        
        
class BookSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=Book
        fields='__all__'