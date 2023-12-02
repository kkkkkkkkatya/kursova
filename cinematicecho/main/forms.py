from .models import Films
from django.forms import ModelForm, TextInput, Textarea, Select


class FilmsForm(ModelForm):
    class Meta:
        model = Films
        year_choices = [(year, int(year)) for year in range(1900, 2024)]
        fields = ["name", "year", "director", "description"]
        widgets = {
            'name' : TextInput(attrs={
            'placeholder' : "Сам удома",
            'class' : "form-control"
        }),
            'year' : Select(choices=year_choices, attrs={
            'placeholder' : "1990",
            'class' : "form-control"
        }),
            'director' : TextInput(attrs={
            'placeholder' : "Кріс Коламбус",
            'class' : "form-control"
        }),
            'description': Textarea(attrs={
                'placeholder': "Восьмирічний Кевін МакКалістер мріє лише про одне...",
                'class': "form-control"
            })
        }
