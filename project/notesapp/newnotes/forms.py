from django.forms import ModelForm

from newnotes.models import FormModel


class DisplayForm(ModelForm):

    class Meta:
        model = FormModel
        fields = [
            'title',
            'description'
        ]
