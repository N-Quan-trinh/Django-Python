from django.db import models


# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=50, default="N/A")
    Author_title = models.CharField(max_length=50, default="N/A")
    Summary = models.CharField(max_length=500, default="N/A")
    Date_published = models.DateTimeField()

    def __str__(self):
        return f'{self.book_title}'


class Platform(models.Model):
    name = models.CharField(max_length=50, default='N/A')
    DateCreated = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'


class Game(models.Model):
    ##
    Genres = [('Ac', 'Action'),
              ('R', 'rpg'),
              ('HR', 'horror'),
              ('JR', 'jrpg'),
              ('ND', 'narative driven')]
    ##
    nameTitle = models.CharField(max_length=30, default='N/A')
    genre = models.CharField(max_length=2, choices=Genres)
    Producers = models.CharField(max_length=50, default='Anonymous')
    Summary = models.TextField(max_length=500, default='N/A')
    platform = models.ForeignKey(Platform, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nameTitle}, By: {self.Producers}'


class UserAccount(models.Model):
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=10)
    email = models.EmailField(default=None)
    RealName = models.CharField(max_length=50)

    def __str__(self):
        return self.UserName
