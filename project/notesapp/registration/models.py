from django.db import models

# Create your models here.

class reg_model (models.Model) :
    name = models.CharField(max_length=25, null= False)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=30, blank=False)
    password = models.CharField(max_length=40, blank= False)
    cnf_password = models.CharField(max_length=40, blank=False)
