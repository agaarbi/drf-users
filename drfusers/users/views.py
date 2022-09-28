from venv import create
from rest_framework.views import APIView

from .serializer import AccountSerializer
from .models import Accounts
from django.contrib.auth.hashers import check_password

from .jwt import get_tokens_for_user, get_user_id, get_access_token
from .responses import *
from .redis_tokens import *


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


class CreateUserWithLogin(APIView):

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                # print(user)
                token = get_tokens_for_user(user)
                # user_id = get_user_id(token.get('access'))
                # print(f"parsed user_id: {user_id}")
                response_field = {"access": token.get('access'), "refresh": token.get(
                    'refresh'), "first_name": user.first_name, "last_name": user.last_name}
                save_token(token.get('access'), str(user))
            else:
                return CustomResponse.error(error_response="USER_DOES_NOT_CREATED", status=ERROR_STATUS_CODE_FORBIDDEN)

        except Exception as err:
            return CustomResponse.internal_server_error(str(err))

        return CustomResponse.success_data(response_field)


create_user_with_login = CreateUserWithLogin.as_view()


class LoginUser(APIView):

    def post(self, request, format=None):
        login_phone = request.data.get('phone')
        login_password = request.data.get('password')

        # get token from header
        # try:
        #     token = get_access_token(request)
        #     print(token)
        # except:
        #     print("token not found in header")

        try:
            user = Accounts.objects.get(phone=login_phone)
            if user:
                if check_password(login_password, user.password):
                    # print(user)
                    # user is itself object that has required uuid
                    token = get_tokens_for_user(user)
                    user_id = get_user_id(token.get('access'))
                    # print(f"parsed user_id: {user_id}")
                    response_field = {"access": token.get('access'), "refresh": token.get(
                        'refresh'), "first_name": user.first_name, "last_name": user.last_name}
                    save_token(token.get('access'), user_id)
                else:
                    return CustomResponse.error_login(error_response="error", wrong_attempts="", status=ERROR_STATUS_CODE)
            else:
                return CustomResponse.error(error_response="error", status=ERROR_STATUS_CODE)

        except Exception as err:
            return CustomResponse.internal_server_error(str(err))

        return CustomResponse.success_data(response_field)


login_user = LoginUser.as_view()


class LogoutUser(APIView):

    def post(self, request, format=None):
        token = request.data.get('token')
        if (delete_token(token)):
            return CustomResponse.success_data("account logged out")
        else:
            return CustomResponse.error(error_response="logout error", status=ERROR_STATUS_CODE)


logout_user = LogoutUser.as_view()
