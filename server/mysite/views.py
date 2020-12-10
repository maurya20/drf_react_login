from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,UserProfile
from .serializers import UserSerializer
# from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignupView(APIView):
    permission_classes = []

    def post(self, request, format=None):
        data = self.request.data
        username = data["username"]
        email = data["email"]
        password = data["password"]
        
        if User.objects.filter(email=email).exists():
            return Response({"error":"Email Already Exists!"})
        else:
            user = User.objects.create(username=username,email=email,password=password)
            user.set_password(password)
            user.save()
            userprofile = UserProfile.objects.create(user=user)
            userprofile.save()
            return Response({"success":"A new user created sucessfully"})