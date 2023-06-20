from django.shortcuts import render,redirect
from newnotes.models import FormModel
from newnotes.forms import DisplayForm
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def home_view(request) :
    data = FormModel.objects.all()
    return render(request, 'home.html', {'data': data})



def delete_notes(request, id) :
    if request.method == 'POST':
        data = FormModel.objects.get(id=id)
        data.delete()
    return redirect('home')


def edit_notes(request, id) :
    data = FormModel.objects.get(id=id)
    form = DisplayForm(instance=data)
    # if request.method == 'POST':
    #     x = DisplayForm()
    #     if x.is_valid():
    #         x.save()
    #         return redirect('home')
    return render(request, 'update.html', {'form': form, 'for_id' : data})

def update_notes(request, id) :
    update = FormModel.objects.get(id = id)
    form = DisplayForm(request.POST, instance=update)
    if form.is_valid():
        form.save()
    return redirect('/')