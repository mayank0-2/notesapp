from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from newnotes.forms import DisplayForm
from django.shortcuts import redirect
# Create your views here.

@login_required
def NewNotes(request) :
    if request.method == 'POST' :
        form = DisplayForm(request.POST)
        if form.is_valid() :
            form.save()
            # return render(request, 'home.html', {})
            return redirect ('/')
            
    else :
        form = DisplayForm()
    return render(request, 'new_notes.html', {'form' : form})

