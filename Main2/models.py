from django.db import models

class product(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    category_id = models.IntegerField()
    image = models.ImageField(upload_to='Main2/static', blank=True)

class category(models.Model):

    category_id = models.IntegerField()
    name = models.CharField(max_length=200)

class Animal(models.Model):

    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self):
        print(f'The {self.name} says "{self.sound}"')
        return f'The {self.name} says "{self.sound}"'

# Create your models here.
