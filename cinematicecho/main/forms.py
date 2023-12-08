from .models import Films, Directors, Actors, Genres
from django.forms import ModelForm, TextInput, Textarea, Select,  ClearableFileInput


def make_list(mod) -> list:
    objs_ch = []
    list = mod.objects.order_by('-id')
    for li in list:
        print(f"li: {li.id} : {li.name}")
        objs_ch.append((li.id, li.name))
    return objs_ch

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        year_choices = [(year, int(year)) for year in range(1900, 2024)]
        directors_choices = Directors.objects.order_by('-id')

        fields = ["name", "year", "director", "description", "images"]
        widgets = {
            'name' : TextInput(attrs={
            'placeholder' : "Сам удома",
            'class' : "form-control"
        }),
            'year' : Select(choices=year_choices, attrs={
            'placeholder' : "1990",
            'class' : "form-control"
        }),
            'director' : Select(choices=directors_choices, attrs={
            'placeholder' : "Кріс Коламбус",
            'class' : "form-control"
        }),
            'description': Textarea(attrs={
                'placeholder': "Восьмирічний Кевін МакКалістер мріє лише про одне...",
                'class': "form-control"
        }),
            'images': ClearableFileInput(attrs={
                'placeholder': "select image",
                'class': "form-control"
            })
        }



class SelectActorsForm(ModelForm):
    class Meta:
        model = Actors

        actors_choices = make_list(model)
        print(f"actors_choices: {actors_choices}")

        fields = ["name"]
        widgets = {
            'name' : Select(choices=actors_choices, attrs={
            'placeholder' : "Маколей Калкін",
            'class' : "form-control"
        })
        }


class SelectGenresForm(ModelForm):
    class Meta:
        model = Genres

        genres_choices = make_list(model)
        print(f"actors_choices: {genres_choices}")

        fields = ["name"]
        widgets = {
            'name' : Select(choices=genres_choices, attrs={
            'placeholder' : "комедія",
            'class' : "form-control"
        })
        }