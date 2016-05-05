from django.db import models
from django.utils import timezone
from django.contrib import admin

class ContainerType(models.Model):
  name = models.CharField(max_length = 64)

  def __str__(self):
    return self.name

class Nutrition(models.Model):
  name = models.CharField(max_length = 64)
  calories_per_g = models.FloatField(default = 0)

  def __str__(self):
    return "%s (%.1f kcal / g)" % (self.name, self.calories_per_g)

class Food(models.Model):
  name = models.CharField(max_length = 64)
  nutritions = models.ManyToManyField(Nutrition, through='Composition')
  ean_code = models.CharField(max_length = 13, blank = True, default = None)
  is_fluid = models.BooleanField(default = False)
  container_types = models.ManyToManyField(ContainerType, through='Packages')

  def __str__(self):
    return self.name

class Composition(models.Model):
  nutrition = models.ForeignKey(Nutrition)
  food = models.ForeignKey(Food)
  ammount_per_100_units = models.FloatField(default = 0)

  class Meta:
    unique_together = ('nutrition', 'food',)

  def __str__(self):
    return "%s (%dg)" % (self.nutrition.name, self.ammount_per_100_units)

class CompositionInline(admin.TabularInline):
  model = Composition
  extra = 1

class Packages(models.Model):
  container_types = models.ForeignKey(ContainerType)
  food = models.ForeignKey(Food)
  ammount_units = models.FloatField(default = 1)

  class Meta:
    unique_together = ('container_types', 'food')

  def __str__(self):
    return "%s (%d)" % (self.container_types.name, self.ammount_units)

class PackagesInline(admin.TabularInline):
  model = Packages
  extra = 1

class Meal(models.Model):
  date = models.DateField()
  food = models.ForeignKey(Food)
  packages = models.ForeignKey(Packages)
  ammount = models.FloatField(default = 1)

  def __str__(self):
    return "%s @ %d kCals" % (self.food.name, 200)

class Store(models.Model):
  name = models.CharField(max_length = 64)

  def __str__(self):
    return self.name

