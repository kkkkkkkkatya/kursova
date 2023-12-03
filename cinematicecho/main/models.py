from django.db import models

# Create your models here.
class Genres(models.Model):
    name = models.CharField('Назва', max_length=30)

    def __str__(self):
        return self.name

class Directors(models.Model):
    name = models.CharField('Ім\'я', max_length=100)
    description = models.TextField('Опис')

    def __str__(self):
        return self.name

class Actors(models.Model):
    name = models.CharField('Ім\'я', max_length=100)
    description = models.TextField('Опис')

    def __str__(self):
        return self.name


class Films(models.Model):
    name = models.CharField('Назва', max_length=100)
    year = models.IntegerField('Рік', blank=True, null=True)
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)
    description = models.TextField('Опис')

    def __str__(self):
        return 'Назва фільму: ' + self.name


class RelFilmsActors(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)