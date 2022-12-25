from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer, ContactSerializer


# Create your views here.
@api_view(["POST", "PUT"])
def subscribe(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST", "PUT"])
def unsubscribe(request, id):
    user = UserSerializer(data=request.data, id=id)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_202_ACCEPTED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def contact(request):
    cxt = ContactSerializer(data=request.data)
    if cxt.is_valid():
        cxt.save()
        return Response(cxt.data, status=status.HTTP_201_CREATED)
    return Response(cxt.errors, status=status.HTTP_400_BAD_REQUEST)