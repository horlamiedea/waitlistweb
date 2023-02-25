from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import WaitListSerializers, RiderRegisterSerializers
from rest_framework.response import Response
from .models import WaitList
# Create your views here.



class WaitListView(generics.GenericAPIView):
    
    serializer_class = WaitListSerializers
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            created = serializer.save()
            return Response('email sent successfully', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiderRegisterView(generics.GenericAPIView):
    
    serializer_class = RiderRegisterSerializers
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            created = serializer.save()
            return Response('Registered successfully', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

