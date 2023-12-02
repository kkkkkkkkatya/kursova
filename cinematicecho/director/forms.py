from main.models import Directors
from django.forms import ModelForm, TextInput, Textarea, Select


class DirectorsForm(ModelForm):
    class Meta:
        model = Directors
        fields = ["name", "description"]
        widgets = {
            'name' : TextInput(attrs={
            'placeholder' : "Кріс Коламбус",
            'class' : "form-control"
        }),
            'description': Textarea(attrs={
                'placeholder': "Американский кінорежисер, сценарист, продюсер...",
                'class': "form-control"
            })
        }
