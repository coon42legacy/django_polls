from django.shortcuts import render
from django.contrib import admin
from .models import CompositionInline, PackagesInline
from .models import Meal
from django.views import generic
from django.utils import timezone
from django.db.models import Sum

class IndexView(generic.ListView):
  template_name = 'myFood/index.html'
  context_object_name = 'meals_list'

  def get_queryset(self):
    return Meal.objects.annotate(Sum('ammount'))

class NutritionAdmin(admin.ModelAdmin):
  inlines = (CompositionInline,)

class FoodAdmin(admin.ModelAdmin):
  inlines = (CompositionInline,PackagesInline,)

class ContainerTypeAdmin(admin.ModelAdmin):
  inlines = (PackagesInline,)

