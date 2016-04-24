from django.db import models
from django.utils import timezone

class Nutrition(models.Model):
  name = models.CharField(max_length = 64)

  def __str__(self):
    return self.name

class Food(models.Model):
  name = models.CharField(max_length = 64)
  nutritions = models.ManyToManyField(Nutrition, through='Composition')

  def __str__(self):
    return self.name

class Composition(models.Model):
  nutrition = models.ForeignKey(Nutrition)
  food = models.ForeignKey(Food)
  ammount = models.IntegerField(default = 0)

class Store(models.Model):
  name = models.CharField(max_length = 64)

  def __str__(self):
    return self.name

