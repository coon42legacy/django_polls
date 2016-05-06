from django.shortcuts import render
from django.contrib import admin
from .models import CompositionInline, PackagesInline
from .models import Meal
from django.views import generic
from django.utils import timezone
from django.db.models import Sum

def Index(request):
  meals_list = Meal.objects.all().filter(date = timezone.now())

  for meal in meals_list:
    for nutrition, ammount in meal.kcals_of_nutritions().items():
      setattr(meal, "kcal_" + nutrition, ammount)

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

