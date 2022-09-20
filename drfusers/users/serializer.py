from rest_framework import serializers

from .models import Accounts


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = [
            'phone',
            'email',
            'password',
            'first_name',
            'last_name',
        ]


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)
    password = serializers.CharField(max_length=300)


# JSON Query for writing user details in custom accounts db
"""{
"phone":"03002588822",
"email":"agaarbi@gmail.com",
"password": "1234", 
"first_name": "abdul",
"last_name": "ghani"
}"""
