from django.shortcuts import render
from rest_framework import serializers
from .serializers import Notes_serializer
from newnotes.models import FormModel
from rest_framework.response import Response 
from rest_framework.views import APIView



# Create your views here.


class serializer_view(APIView): 
    def get(self, request, format = None):
        obj = FormModel.objects.all() 
        serializer = Notes_serializer(obj, many=True)
        return Response(serializer.data)
    
    