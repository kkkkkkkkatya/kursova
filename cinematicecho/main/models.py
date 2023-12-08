from django.db import models

# Create your models here.
class Genres(models.Model):
    name = models.CharField('Назва', max_length=30)
    description = models.TextField('Опис', blank=True, null=True)

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
    # file will be uploaded to MEDIA_ROOT/images
    images = models.ImageField(upload_to="images/", blank=True, null=True)



    def __str__(self):
        return 'Назва фільму: ' + self.name


class RelFilmsActors(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('film', 'actor')
        #ordering = ['-actor']


class RelFilmsGenres(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('film', 'genre')
        #ordering = ['-actor']

