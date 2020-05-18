from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import User_Model, Activity_Period_Model
from . serializers import User_Model_serializer, Activity_Period_Model_serializer
from rest_framework.generics import ListAPIView

# Create your views here.

class user_list(APIView):

    def get(self, request):

        user1 =  User_Model.objects.all()
        serializer = User_Model_serializer(user1, many= True)
        return Response(serializer.data)
        

class activity_list(APIView):

    def get(self, request):

        activity1 =  Activity_Period_Model.objects.all()
        serializer = Activity_Period_Model_serializer(activity1, many= True)
        return Response(serializer.data)

class CombineListView(ListAPIView):
    serializer_class_Equity = User_Model_serializer
    serializer_class_Fno = Activity_Period_Model_serializer

    def get_queryset_Equity(self):
        return User_Model.objects.all()
        

    def get_queryset_Fno(self):
        return Activity_Period_Model.objects.all()

    def list(self, request, *args, **kwargs):
        fno = self.serializer_class_Fno(self.get_queryset_Fno(), many=True)
        equity = self.serializer_class_Equity(self.get_queryset_Equity(), many=True)
        return Response({
            "**User_Model**": equity.data,
            "**Activity_Period_Model**": fno.data
        })




