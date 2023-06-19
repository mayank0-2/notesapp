from django.shortcuts import render
from rest_framework import serializers
from .serializers import Notes_serializer
from newnotes.models import FormModel
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.


class serializer_view(APIView): 
    
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self, request, format = None):
        obj = FormModel.objects.all() 
        serializer = Notes_serializer(obj, many=True)
        return Response(serializer.data)
    
    
    def put(self, request, format = None):
        instance = request.data
        serializer = Notes_serializer(instance, many=True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(status.error)    
    
