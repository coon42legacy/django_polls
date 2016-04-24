from django.shortcuts import render

from django.contrib import admin
from .models import CompositionInline

class NutritionAdmin(admin.ModelAdmin):
  inlines = (CompositionInline,)

class FoodAdmin(admin.ModelAdmin):
  inlines = (CompositionInline,)

