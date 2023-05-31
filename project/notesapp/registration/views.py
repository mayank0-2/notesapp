from django.shortcuts import redirect, render
from registration.forms import reg_form

# Create your views here.

def register(request) :
    if request.method == 'POST' :
        form = reg_form(request.POST)
        if form.is_valid() :
            redirect ('home.html')
    else :
        form = reg_form()

    return render(request, 'register.html', {'form': form})
