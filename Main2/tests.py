from django.test import TestCase
from .models import Animal

class MyTestAnimal(TestCase):
    def setUp(self):
        Animal.objects.create(name='Leon', sound='roar')
        Animal.objects.create(name='Cat', sound='miau')

    def test_animals_can_speak(self):
        Leon = Animal.objects.get(name='Leon')
        Cat = Animal.objects.get(name='Cat')
        self.assertEqual(Leon.speak(), 'The Leon says "roar"')
        self.assertEqual(Cat.speak(), 'The Cat says "miau"')

# Some changes made for GIT status track        

# Create your tests here.
