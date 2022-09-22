from rest_framework_simplejwt.tokens import RefreshToken
import jwt


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def get_user_id(token):
    payload = jwt.decode(token, algorithms=["HS256"], options={
                         "verify_signature": False})
    # print(payload)
    parsed_user_id = payload["user_id"]
    # print(f"parsed user_id is: {parsed_user_id}")
    return parsed_user_id


def get_access_token(request):
    headers = request.headers
    # print(headers)
    bearer = headers.get('Authorization')    # Bearer YourTokenHere
    token = bearer.split()[1]  # YourTokenHere
    return token
