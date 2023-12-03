from django.shortcuts import render
from main.models import Directors
from main.keeper_service import keeper_service
from .forms import DirectorsForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
app_name = "director"

### film list for admins ###
def list(request):
    error = keeper_service.pop("error")
    instance_list = Directors.objects.order_by('-id')
    return render(request, f'{app_name}/list.html', {'instance_list':instance_list, 'error':error})

### create film ###
def create(request):
    print(f"=== {app_name}, action: create === ")
    error= ''
    if request.method == "POST":
        form = DirectorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'{app_name}:list')
        else:
            error = 'Помилки при заповненні форми'

    form = DirectorsForm()
    context = {
        'form' : form,
        'error' : error
    }
    return render(request, f'{app_name}/create.html', context)

### edit film ###
def edit(request, id):
    print(f"=== {app_name}, action: edit === ")
    print(f"id: ", id)
    error = ''

    instance = get_object_or_404(Directors, id=id)

    ### update film
    if request.method == 'POST':
        form = DirectorsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(f'{app_name}:show', id=instance.id)  # Redirect to film detail view
        else:
            error = 'Помилки при заповненні форми'

    ### open form for updating
    else:
        form = DirectorsForm(instance=instance)

    return render(request, f'{app_name}/edit.html', {'form': form, 'error':error})



### delete film ###
def delete(request, id):
    print(f"=== {app_name}, action: delete === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = Directors.objects.get(id=id)
        print(f"obj: {obj}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")

    return redirect(f'{app_name}:list')


### show film ###
def show(request, id):
    print(f"=== {app_name}, action: show === ")
    print(f"id: ", id)
    error = ''

    instance = get_object_or_404(Directors, id=id)
    form = DirectorsForm(instance=instance)

    return render(request, f'{app_name}/show.html', {'form': form, 'error':error, 'id':id})
