from django.shortcuts import render
from newnotes.models import FormModel
# Create your views here.


def home_view(request) :
    if request.user.is_authenticated :
        data = FormModel.objects.all()
    else :
        data = None
    return render(request, 'home.html', {'data': data})
