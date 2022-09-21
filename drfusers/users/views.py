from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import AccountSerializer
from .models import Accounts
from django.contrib.auth.hashers import check_password

from .jwt import get_tokens_for_user


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

    login_phone = request.data.get('phone')
    login_password = request.data.get('password')

    user = Accounts.objects.get(phone=login_phone)
    if user:
        print(user.password)
        if check_password(login_password, user.password):
            print("password validated")
            token = get_tokens_for_user(user)
            print(token)
            response_field = {"access": token.get('access'), "refresh": token.get(
                'refresh'), "first_name": user.first_name, "last_name": user.last_name}
        else:
            print("invalid password")
    else:
        print("invalid phone number")

    return Response(response_field)
