from venv import create
from rest_framework.decorators import api_view

from .serializer import AccountSerializer
from .models import Accounts
from django.contrib.auth.hashers import check_password

from .jwt import get_tokens_for_user, get_user_id
from .responses import *


@api_view(['POST'])
def create_user(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # print(serializer.data)
        return CustomResponse.create()
    else:
        return CustomResponse.error(error_response="USER_DOES_NOT_CREATED", status=ERROR_STATUS_CODE_FORBIDDEN)


@api_view(['POST'])
def login_user(request):

    login_phone = request.data.get('phone')
    login_password = request.data.get('password')

    try:
        user = Accounts.objects.get(phone=login_phone)
        if user:
            if check_password(login_password, user.password):
                token = get_tokens_for_user(user)
                # user_id = get_user_id(token.get('access'))
                # print(f"parsed user_id: {user_id}")
                response_field = {"access": token.get('access'), "refresh": token.get(
                    'refresh'), "first_name": user.first_name, "last_name": user.last_name}
            else:
                return CustomResponse.error_login(error_response="error", wrong_attempts="", status=ERROR_STATUS_CODE)
        else:
            return CustomResponse.error(error_response="error", status=ERROR_STATUS_CODE)

    except Exception as err:
        return CustomResponse.internal_server_error(str(err))

    return CustomResponse.success_data(response_field)
