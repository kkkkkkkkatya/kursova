from main.models import Actors
from django.forms import ModelForm, TextInput, Textarea, Select


class ActorsForm(ModelForm):
    class Meta:
        model = Actors
        fields = ["name", "description"]
        widgets = {
            'name' : TextInput(attrs={
            'placeholder' : "Маколей Калкін",
            'class' : "form-control"
        }),
            'description': Textarea(attrs={
                'placeholder': "Американський актор, один з найуспішніших дітей-акторів...",
                'class': "form-control"
            })
        }
