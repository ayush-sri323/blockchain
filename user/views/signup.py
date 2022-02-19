from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


@permission_classes((AllowAny,))
class SignupView(GenericAPIView):
    @csrf_exempt
    def post(self, request):
        return Response("",status=HTTP_200_OK)
