from django.shortcuts import render, redirect, get_object_or_404
from .models import Films, RelFilmsActors, Actors
from .forms import FilmsForm, SelectActorsForm
from .keeper_service import keeper_service


# Create your CONTROLLERS here.

### film list for users ###
def index(request):
    film_list = Films.objects.order_by('-id')
    return render(request, 'main/index.html', {'film_list':film_list})

### about site ###
def about(request):
    return render(request, 'main/about.html')

### film list for admins ###
def list(request):
    error = keeper_service.pop("error")
    film_list = Films.objects.order_by('-id')
    return render(request, 'main/list.html', {'film_list':film_list, 'error':error})

### create film ###
def create(request):
    print(f"=== main, action: create === ")
    error= ''
    if request.method == "POST":
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:list')
        else:
            error = 'Помилки при заповненні форми'

    form = FilmsForm()
    context = {
        'form' : form,
        'error' : error
    }
    return render(request, 'main/create.html', context)

### edit film ###
def edit(request, id):
    print(f"=== main, action: edit === ")
    print(f"id: ", id)
    print(f"method: ", request.method)
    error = ''

    film = get_object_or_404(Films, id=id)

    ### update film
    if request.method == 'POST':
        form = FilmsForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('main:show', id=film.id)  # Redirect to film detail view
        else:
            error = 'Помилки при заповненні форми'

    ### open form for updating
    else:
        form = FilmsForm(instance=film)

    return render(request, 'main/edit.html', {'form': form, 'error':error})



### delete film ###
def delete(request, id):
    print(f"=== main, action: delete === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = Films.objects.get(id=id)
        print(f"obj: {obj}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")

    return redirect('main:list')


### show film ###
def show(request, id):
    print(f"=== main, action: show === ")
    print(f"id: ", id)
    error = ''

    film = get_object_or_404(Films, id=id)
    form = FilmsForm(instance=film)
    actors_form = SelectActorsForm()
    #actors_list = RelFilmsActors.objects.filter(film=id)
    sql = f"""select a.id , a.name
             from main_relfilmsactors r
                  join main_actors a on a.id = r.actor_id
                  where r.film_id = {id}"""
    actors_list = RelFilmsActors.objects.raw(sql)

    return render(request, 'main/show.html',
                  {'form': form, 'error':error, 'id':id,
                   'actors_list':actors_list, 'actors_form': actors_form })



def add_actor(request):
    print(f"=== main, action: add-actor === ")
    #print(f"request: {request.POST.dict() } ")
    film_id = request.POST.dict()['id']
    actor_id = request.POST.dict()['name']
    print(f"film_id: {film_id}, actor_id: {actor_id} ")
    error = ''

    instance = RelFilmsActors()
    instance.film = Films.objects.get(id=film_id)
    instance.actor = Actors.objects.get(id=actor_id)
    instance.save(force_insert=True)
    return redirect('main:show', id=film_id)