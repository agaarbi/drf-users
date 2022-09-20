from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import AccountSerializer

# Create your views here.


@api_view(['POST'])
def create_user(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        return Response({"status": "user registered"})
    else:
        return Response({"invalid": "criteria not match"})
