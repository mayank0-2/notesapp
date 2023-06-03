from django import forms
from django.forms import ModelForm
from registration.models import reg_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

# class reg_form(ModelForm) : 
class reg_form(UserCreationForm) :
    class Meta:
        # model = reg_model
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'                    
        ]
