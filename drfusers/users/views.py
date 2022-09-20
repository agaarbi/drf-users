from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import AccountSerializer, LoginSerializer
from .models import Accounts
from django.contrib.auth.hashers import check_password

from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def create_user(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        return Response({"status": "user registered"})
    else:
        return Response({"invalid": "criteria not match"})


@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        login_phone = serializer.data.get('phone')
        login_password = serializer.data.get('password')
        queryset = Accounts.objects.filter(phone=login_phone)
        if queryset:
            print(queryset[0].password)
            if check_password(login_password, queryset[0].password):
                print("password validated")
                token = get_tokens_for_user(queryset[0])
                print(token)
                response_field = {"access": token.get('access'), "refresh": token.get(
                    'refresh'), "first_name": queryset[0].first_name, "last_name": queryset[0].last_name}
            else:
                print("invalid password")
        else:
            print("invalid phone number")
        return Response(response_field)
    else:
        return Response({"invalid": "criteria not match"})


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
