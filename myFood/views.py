from django.shortcuts import render
from django.contrib import admin
from .models import CompositionInline, PackagesInline
from .models import Meal
from django.views import generic
from django.utils import timezone
from django.db.models import Sum

def Index(request):
  meals_list = Meal.objects.all()

  for meal in meals_list:
    kcal_total = 0

    for c in meal.food.composition_set.all():
      kcal = meal.ammount * c.nutrition.calories_per_g * \
        c.ammount_per_100_units * meal.packages.ammount_units / 100.0

      kcal_total += kcal
      setattr(meal, "kcal_" + c.nutrition.name, int(kcal))

    meal.kcal_total = int(kcal_total)

  context = {
    'meals_list': meals_list,
  }

  return render(request, 'myFood/index.html', context)

class NutritionAdmin(admin.ModelAdmin):
  inlines = (CompositionInline,)

class FoodAdmin(admin.ModelAdmin):
  inlines = (CompositionInline,PackagesInline,)

class ContainerTypeAdmin(admin.ModelAdmin):
  inlines = (PackagesInline,)

