from django.urls import path
from . import views


urlpatterns = [
    path('', views.list, name='actors'),
    path('/create', views.create, name='create'),
    path('/list', views.list, name='list'),
    path('/show/<int:id>', views.show, name='show'),
    path('/delete/<int:id>', views.delete, name='delete'),
    path('/edit/<int:id>', views.edit, name='edit')

]
