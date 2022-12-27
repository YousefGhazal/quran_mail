from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from main.models import User
from .serializers import UserSerializer, ContactSerializer


# Create your views here.
@api_view(["POST", "PUT"])
def subscribe(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def unsubscribe(request, email):
    user = User.objects.get(email=email)
    ser = UserSerializer(instance=user, data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# def unsubscribe(request, email):
#     user = User.objects.get(email=email)
#     user.active = False
#     user.save()
#     return Response(status=status.HTTP_202_ACCEPTED)


@api_view(["POST"])
def contact(request):
    ser = ContactSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)