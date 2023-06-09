from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import FormModel

class Notes_serializer(serializers.ModelSerializer):
    class Meta:
            model = FormModel
            fields = '__all__'