from django.contrib import admin

from .models import Nutrition, Food, Composition, Store

admin.site.register(Nutrition)
admin.site.register(Food)
admin.site.register(Composition)
admin.site.register(Store)
