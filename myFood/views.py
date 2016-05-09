from django.shortcuts import render
from django.contrib import admin
from .models import CompositionInline, PackagesInline
from .models import Meal, Nutrition
from django.views import generic
from django.utils import timezone

def Index(request):
  meals_list = Meal.objects.all().filter(date = timezone.now())
  nutrition_names = [n.name for n in Nutrition.objects.all()]

  for nutrition in nutrition_names:
    setattr(meals_list, "kcal_" + nutrition, 0)

  for meal in meals_list:
    for nutrition in nutrition_names:
      setattr(meal, "kcal_" + nutrition, "N/A")

    for nutrition, ammount in meal.kcals_of_nutritions().items():
      setattr(meal, "kcal_" + nutrition, ammount)
      setattr(meals_list, "kcal_" + nutrition, getattr(meals_list, "kcal_" + nutrition) + ammount)

  meals_list.kcal_total = sum([getattr(meals_list, "kcal_" + n) for n in nutrition_names])

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

