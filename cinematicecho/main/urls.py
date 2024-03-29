from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('list', views.list, name='list'),
    path('create', views.create, name='create'),
    path('show/<int:id>', views.show, name='show'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('add_actor', views.add_actor, name='add_actor'),
    path('delete_actor/<int:id>', views.delete_actor, name='delete_actor'),
    path('add_genre', views.add_genre, name='add_genre'),
    path('delete_genre/<int:id>', views.delete_genre, name='delete_genre'),
    path('a_film/<int:id>', views.a_film, name='a_film'),
]
