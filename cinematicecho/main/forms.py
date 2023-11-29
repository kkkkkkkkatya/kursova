from .models import Films
from django.forms import ModelForm, TextInput, Textarea


class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ["name", "description"]
        widgets = {
            'name' : TextInput(attrs={
            'placeholder' : "Челюсті 3",
            'class' : "form-control"
        }),
            'description': Textarea(attrs={
                'placeholder': "У далекому 2005 році було знято...",
                'class': "form-control"
            })
        }
