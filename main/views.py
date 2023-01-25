from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from main.models import User

from .serializers import ContactSerializer, UserSerializer, UserUnsubSerializer


# Create your views here.
@swagger_auto_schema(
        operation_description="""""",
        request_body=UserSerializer,
        method='POST'
    )
@api_view(["POST"])
def subscribe(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
        operation_description="""""",
        request_body=UserUnsubSerializer,
        method='POST'
    )
@api_view(["POST"])
def unsubscribe(request, id):
    # user = User.objects.get(id=id)
    user = get_object_or_404(User, id=id)
    ser = UserUnsubSerializer(instance=user, data=request.data)
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

@swagger_auto_schema(
        operation_description="""""",
        request_body=ContactSerializer,
        method='POST'
    )
@api_view(["POST"])
def contact(request):
    ser = ContactSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)