from venv import create
from rest_framework.views import APIView

from .serializer import AccountSerializer
from .models import Accounts
from django.contrib.auth.hashers import check_password

from .jwt import get_tokens_for_user, get_user_id
from .responses import *


class CreateUser(APIView):

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # print(serializer.data)
            return CustomResponse.create()
        else:
            return CustomResponse.error(error_response="USER_DOES_NOT_CREATED", status=ERROR_STATUS_CODE_FORBIDDEN)


create_user = CreateUser.as_view()


class LoginUser(APIView):

    def post(self, request, format=None):
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


login_user = LoginUser.as_view()
