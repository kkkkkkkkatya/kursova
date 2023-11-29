from django.shortcuts import render, redirect
from .models import Films
from .forms import FilmsForm


# Create your views here.
def index(request):
    film_list = Films.objects.all()
    return render(request, 'main/index.html', {'film_list':film_list})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error= ''
    if request.method == "POST":
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Помилки при заповненні форми'

    form = FilmsForm()
    context = {
        'form' : form,
        'error' : error
    }
    return render(request, 'main/create.html', context)
