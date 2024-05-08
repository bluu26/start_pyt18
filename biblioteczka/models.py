from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField("Genre") #pracuje na tabelce posredniej


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

