from django.db import models
from django.utils import timezone
from django.contrib import admin

class ContainerType(models.Model):
  name = models.CharField(max_length = 64, unique = True)

  def __str__(self):
    return self.name

class Nutrition(models.Model):
  name = models.CharField(max_length = 64, unique = True)
  calories_per_g = models.FloatField(default = 0)

  def __str__(self):
    return "%s (%.1f kcal / g)" % (self.name, self.calories_per_g)

class Manufacturer(models.Model):
  name = models.CharField(max_length = 64)

  def __str__(self):
    return "%s" % self.name

class Food(models.Model):
  name = models.CharField(max_length = 64, unique = True)
  manufacturer = models.ForeignKey(Manufacturer, null = True, blank = True)
  nutritions = models.ManyToManyField(Nutrition, through='Composition')
  ean_code = models.CharField(max_length = 13, blank = True, null = True, default = None)
  is_fluid = models.BooleanField(default = False)
  nutritions_veryfied = models.BooleanField(default = False)
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

  def kcals_of_nutritions(self):
    kcals_meal = {}

    for c in self.food.composition_set.all():
      kcals_meal[c.nutrition.name] = int((
          self.ammount *                  \
          self.packages.ammount_units *   \
          c.nutrition.calories_per_g *    \
          c.ammount_per_100_units) /      \
          100.0                           \
      )

    return kcals_meal

  def kcal_total(self):
    return sum([kcals for kcals in self.kcals_of_nutritions().values()])

  def __str__(self):
    return "%s: %s @ %d kCals" % (self.date.isoformat(), self.food.name,
            self.kcal_total())

class Store(models.Model):
  name = models.CharField(max_length = 64)

  def __str__(self):
    return self.name

