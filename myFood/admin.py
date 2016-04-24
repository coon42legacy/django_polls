from django.contrib import admin

from .models import Nutrition, Food, Composition, Store
from .views import NutritionAdmin, FoodAdmin

admin.site.register(Store)
admin.site.register(Food, FoodAdmin)
admin.site.register(Nutrition, NutritionAdmin) 

