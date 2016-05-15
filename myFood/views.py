from django.shortcuts import render
from django.contrib import admin
from .models import CompositionInline, PackagesInline
from .models import Meal, Nutrition
from django.views import generic
from django.utils import timezone

def Index(request):
  meals_list = Meal.objects.all().filter(date = timezone.now())
  nutrition_names = [n.name for n in Nutrition.objects.all()]
  meals_list.kcal = {}
  meals_list.percent = {}
  meals_list.grams = {}

  # TODO: replace following code with:
  #  - calculate kcals
  #  - calculate percents
  #  - calculate grams

  for nutrition in nutrition_names:
    meals_list.kcal[nutrition] = 0
    meals_list.grams[nutrition] = 0

  for meal in meals_list:
    meal.kcal = {}
    meal.kcal["total"] = 0

    for nutrition in nutrition_names:
      meal.kcal[nutrition] = "N/A"

    for nutrition, ammount in meal.kcals_of_nutritions().items():
      meal.kcal[nutrition] = ammount
      meals_list.kcal[nutrition] += ammount
      meal.kcal["total"] += ammount

  meals_list.kcal["total"] = sum([meals_list.kcal[n] for n in nutrition_names])

  for nutrition in Nutrition.objects.all():
    kcal_total = meals_list.kcal[nutrition.name]
    percent_total = kcal_total * 100 / meals_list.kcal["total"] if kcal_total > 0 else 0

    if kcal_total:
      meals_list.percent[nutrition.name] = "%.2f" % percent_total
      meals_list.grams[nutrition.name] = "-" # TODO: replace by grams

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

