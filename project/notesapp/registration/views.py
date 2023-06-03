from django.shortcuts import render
from registration.forms import reg_form
from django.http import HttpResponseRedirect
# Create your views here.

def register(request) :
    if request.method == 'POST' :
        form = reg_form(request.POST)
        if form.is_valid() :
            form.save()
            return render(request, 'home.html', {})

    else :
        form = reg_form()

    return render(request, 'register.html', {'form': form})

