from django.shortcuts import redirect, render
from registration.forms import reg_form

# Create your views here.

def register(request) :
    if request.method == 'POST' :
        form = reg_form(request.POST)
        if form.is_valid() :
            form.save()
            redirect ('home.html')

    else :
        form = reg_form()
        redirect('register.html')

    return render(request, 'register.html', {'form': form})
