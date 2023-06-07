from django.shortcuts import render,redirect
from newnotes.models import FormModel


# Create your views here.


def home_view(request) :
    if request.user.is_authenticated :
        data = FormModel.objects.all()
    else :
        data = None
    return render(request, 'home.html', {'data': data})



def delete_notes(request, id) :
    if request.method == 'POST':
        data = FormModel.objects.get(id=id)
        data.delete()
    return redirect('home') 


def edit_notes(request, id) :
    if request.method == 'POST':
        pass
    
    return redirect('home')