from django.shortcuts import render, redirect, get_object_or_404
from .models import Films, RelFilmsActors, Actors, RelFilmsGenres, Genres
from .forms import FilmsForm, SelectActorsForm, SelectGenresForm
from .keeper_service import keeper_service
from cinematicecho.settings import MEDIA_ROOT


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
    action="create"

    if request.method == "POST":
        form = FilmsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:list')
        else:
            error = 'Помилки при заповненні форми'

    form = FilmsForm()
    context = {
        'form' : form,
        'error' : error,
        'action' : action
    }
    return render(request, 'main/create.html', context)


### edit film ###
def edit(request, id):
    print(f"=== main, action: edit === ")
    print(f"id: ", id)
    print(f"method: ", request.method)
    error = ''
    cur_action = "edit"

    film = get_object_or_404(Films, id=id)

    actors_form = SelectActorsForm()
    # actors_list = RelFilmsActors.objects.filter(film=id)
    sql = f"""select a.id , a.name, r.id as rel_id
                 from main_relfilmsactors r
                      join main_actors a on a.id = r.actor_id
                      where r.film_id = {id}"""
    actors_list = RelFilmsActors.objects.raw(sql)

    genres_form = SelectGenresForm()
    sql = f"""select g.id , g.name, fg.id as rel_id
                 from main_relfilmsgenres fg
                      join main_genres g on g.id = fg.genre_id
                      where fg.film_id = {id}"""
    genres_list = RelFilmsGenres.objects.raw(sql)

    ### update film
    if request.method == 'POST':
        params = request.POST.dict()
        print(f"params: {params}")
        form = FilmsForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('main:show', id=film.id)  # Redirect to film detail view
        else:
            error = 'Помилки при заповненні форми'
            print('Помилки при заповненні форми')

    ### open form for updating
    else:
        form = FilmsForm(instance=film)

    image_url = ""
    if str(film.images) != "":
        print(f"image.url: {film.images.url}")
        image_url = film.images.url

    return render(request, 'main/edit.html',
                  {'form': form, 'error':error, 'actors_list':actors_list,
                   'actors_form':actors_form, 'genres_form':genres_form,
                   'genres_list':genres_list , 'id':id,
                   'image_url':image_url, 'cur_action':cur_action})



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
    action= "show"
    error = keeper_service.pop("error")

    film = get_object_or_404(Films, id=id)
    form = FilmsForm(instance=film)

    image_url = ""
    if str(film.images) != "":
        print(f"image.url: {film.images.url}")
        image_url = film.images.url


    #actors_list = RelFilmsActors.objects.filter(film=id)
    sql = f"""select a.id , a.name, r.id as rel_id
             from main_relfilmsactors r
                  join main_actors a on a.id = r.actor_id
                  where r.film_id = {id}"""
    actors_list = RelFilmsActors.objects.raw(sql)


    sql = f"""select g.id , g.name, fg.id as rel_id
             from main_relfilmsgenres fg
                  join main_genres g on g.id = fg.genre_id
                  where fg.film_id = {id}"""
    genres_list = RelFilmsGenres.objects.raw(sql)

    return render(request, 'main/show.html',
                  {'form': form, 'error':error, 'id':id,
                   'actors_list':actors_list , 'genres_list':genres_list ,
                   'image_url':image_url, 'action':action})



def add_actor(request):
    print(f"=== main, action: add-actor === ")
    #print(f"request: {request.POST.dict() } ")
    film_id = request.POST.dict()['id']
    actor_id = request.POST.dict()['name']
    print(f"film_id: {film_id}, actor_id: {actor_id} ")
    error = ''

    try:
        instance = RelFilmsActors()
        instance.film = Films.objects.get(id=film_id)
        instance.actor = Actors.objects.get(id=actor_id)
        instance.save(force_insert=True)
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")
    return redirect('main:show', id=film_id)

def delete_actor(request, id):
    print(f"=== main, action: delete_actor === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = RelFilmsActors.objects.get(id=id)
        print(f"obj: {obj}")
        film_id = int(obj.film.id)
        print(f"film_id: {film_id}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")
        return redirect('main:list')

    return redirect('main:show', id=film_id)


def add_genre(request):
    print(f"=== main, action: add-genre === ")
    #print(f"request: {request.POST.dict() } ")
    film_id = request.POST.dict()['id']
    genre_id = request.POST.dict()['name']
    print(f"film_id: {film_id}, actor_id: {genre_id} ")
    error = ''

    try:
        instance = RelFilmsGenres()
        instance.film = Films.objects.get(id=film_id)
        instance.genre = Genres.objects.get(id=genre_id)
        instance.save(force_insert=True)
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")
    return redirect('main:show', id=film_id)

def delete_genre(request, id):
    print(f"=== main, action: delete_genre === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = RelFilmsGenres.objects.get(id=id)
        print(f"obj: {obj}")
        film_id = int(obj.film.id)
        print(f"film_id: {film_id}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")
        return redirect('main:list')

    return redirect('main:show', id=film_id)


### a film ###
def a_film(request, id):
    print(f"=== main, action: a_film === ")
    print(f"id: ", id)
    action= "a_film"
    error = keeper_service.pop("error")

    film = get_object_or_404(Films, id=id)

    image_url = ""
    if str(film.images) != "":
        print(f"image.url: {film.images.url}")
        image_url = film.images.url


    #actors_list = RelFilmsActors.objects.filter(film=id)
    sql = f"""select a.id , a.name, r.id as rel_id
             from main_relfilmsactors r
                  join main_actors a on a.id = r.actor_id
                  where r.film_id = {id}"""
    actors_list = RelFilmsActors.objects.raw(sql)


    sql = f"""select g.id , g.name, g.description, fg.id as rel_id
             from main_relfilmsgenres fg
                  join main_genres g on g.id = fg.genre_id
                  where fg.film_id = {id}"""
    genres_list = RelFilmsGenres.objects.raw(sql)

    return render(request, 'main/a_film.html',
                  {'film': film, 'error':error, 'id':id,
                   'actors_list':actors_list , 'genres_list':genres_list ,
                   'image_url':image_url, 'action':action})

