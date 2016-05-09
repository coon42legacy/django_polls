from django.shortcuts import render
from django.contrib import admin
from .models import CompositionInline, PackagesInline
from .models import Meal, Nutrition
from django.views import generic
from django.utils import timezone

def Index(request):
  meals_list = Meal.objects.all().filter(date = timezone.now())
  nutrition_names = [n.name for n in Nutrition.objects.all()]
  var_prefix = "kcal_"

  for nutrition in nutrition_names:
    setattr(meals_list, var_prefix + nutrition, 0)

  for meal in meals_list:
    for nutrition in nutrition_names:
      setattr(meal, var_prefix + nutrition, "N/A")

    for nutrition, ammount in meal.kcals_of_nutritions().items():
      setattr(meal, var_prefix + nutrition, ammount)
      setattr(meals_list, var_prefix + nutrition, getattr(meals_list, var_prefix + nutrition) + ammount)

  meals_list.kcal_total = sum([getattr(meals_list, var_prefix + n) for n in nutrition_names])

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

