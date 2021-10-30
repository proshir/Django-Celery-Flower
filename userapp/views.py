from django.contrib.auth import authenticate, logout
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.models import Token
from .models import User
# Create your views here.
class LoginPage(generics.GenericAPIView):
    serializer_class=UserSerializer
    def post(self,request):
        if request.user.is_authenticated ==True:
            return Response({"error" : "You logged in before"},status=status.HTTP_400_BAD_REQUEST)
        username=request.data.get("username")
        password=request.data.get("password")
        if not username or not password:
            return Response({"error":"Please fill all fields"},status=status.HTTP_400_BAD_REQUEST)
        check_user=User.objects.filter(username=username).exists()
        if check_user==False:
            return Response({"error":"Username does not exist"},status=status.HTTP_404_NOT_FOUND)
        user=authenticate(username=username,password=password)
        if user is None:
            return Response({"error":"Invalid login details"},status=status.HTTP_400_BAD_REQUEST)
        login(request,user)
        token,created=Token.objects.get_or_create(user=request.user)
        data={
            "token":token.key,
            "user_id":request.user.pk,
            "username":request.user.username
        }
        return Response({"success":"Successfully login","data":data},status=status.HTTP_200_OK)
class LogoutPage(APIView):
    def get(self,request):
        if request.user.is_authenticated ==False:
            return Response({"error" : "You didn't log in before"},status=status.HTTP_400_BAD_REQUEST)
        logout(request)
        return Response({"success" : "You logged out"},status=status.HTTP_200_OK)
