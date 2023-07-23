from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account,AccountDetail
from .serializers import (
                            AccountSerializer,
                            AccountDetailSerializer,
                            LoginSerializer
                        )
# from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class AccountView(generics.CreateAPIView):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_class = [IsAuthenticated]

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        user_id = kwargs.get('user')
        return AccountDetail.objects.get(user=user_id)
    


class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            user = serializer.validated_data['user']
            
            if user is None:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            update_last_login(None, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'username': user.username,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

