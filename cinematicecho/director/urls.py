from django.urls import path
from . import views

#app_name = "director"
urlpatterns = [
    path('', views.list, name='director'),
    path('/create', views.create, name='create'),
    path('/list', views.list, name='list'),
    path('/show/<int:id>', views.show, name='show'),
    path('/delete/<int:id>', views.delete, name='delete'),
    path('/edit/<int:id>', views.edit, name='edit')

]
