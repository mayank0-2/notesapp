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
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : 'Name', 
                'class' : 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline'
                }),

            'username' : forms.TextInput(attrs={
                'placeholder' : 'Username',
                'class' : 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline'
            }),

            'email' : forms.EmailInput({
                'placeholder' : 'Email',
                'class' : 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline'
            }),

            'password' : forms.PasswordInput({
                'placeholder' : 'Password',
                'class' : 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline'
            }),

            'cnf_password' : forms.PasswordInput({
                'placeholder' : 'Confirm Password',
                'class' : 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline'
            })
        }
