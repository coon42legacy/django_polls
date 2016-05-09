from django.contrib import admin

from .models import Nutrition, Food, Composition, Store, Meal, Manufacturer
from .models import ContainerType, Packages


from .views import NutritionAdmin, FoodAdmin, ContainerTypeAdmin

admin.site.register(Store)
admin.site.register(Meal)
admin.site.register(Food, FoodAdmin)
admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(ContainerType, ContainerTypeAdmin)
admin.site.register(Manufacturer)
