from django.shortcuts import render
from registration.forms import reg_form
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from home.views import home_view
# Create your views here.

def register(request) :
    if request.method == 'POST' :
        form = reg_form(request.POST)
        if form.is_valid() :
            form.save()
            user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
            if user is not None :
                login(request, user)
                return home_view(request)
            else :
                return render(request, 'home.html', {})

    else :
        form = reg_form()

    return render(request, 'register.html', {'form': form})



def NewNotes(request) :

    return render(request, 'new_notes.html', {})
