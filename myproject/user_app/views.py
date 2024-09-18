from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message":"Successfully logged out"},status=status.HTTP_200_OK)
    

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Get or create the token for the new user 
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "message": "User registered successfully!",
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
