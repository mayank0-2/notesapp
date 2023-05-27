from django.db import models

# Create your models here.

class reg_user(models.Model):
    name = models.CharField(max_length=25, null = False)
    username = models.CharField(max_length=25, null = False)
    email = models.EmailField(null=False)
    password = models.PasswordInput()
    confirm_password = models.PasswordInput()
