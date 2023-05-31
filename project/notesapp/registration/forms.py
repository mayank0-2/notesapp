from django import forms
from django.forms import ModelForm
from registration.models import reg_model

class reg_form(ModelForm) :
    class Meta:
        model = reg_model
        fields = [
            'name',
            'username',
            'email',
            'password',
            'cnf_password',
            ]
