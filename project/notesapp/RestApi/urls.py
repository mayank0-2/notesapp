from rest_framework import routers
from . views import serializer_view
from django.urls import path 




urlpatterns = [
    path('', serializer_view.as_view()),
]

