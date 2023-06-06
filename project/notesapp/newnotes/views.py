from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from newnotes.forms import DisplayForm
from django.shortcuts import redirect
from newnotes.models import FormModel
# Create your views here.

@login_required
def NewNotes(request) :
    if request.method == 'POST' :
        form = DisplayForm(request.POST)
        if form.is_valid() :
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            data = FormModel.objects.filter(title=title, description=description).exists()
            if data :
                return redirect ('/')
            else :
                form.save()
                return redirect ('/')
            
    else :
        form = DisplayForm()
    return render(request, 'new_notes.html', {'form' : form})

