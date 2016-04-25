from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Food, Nutrition, Composition

class FoodDataBaseTests(TestCase):
  def test_if_nutrition_can_only_be_assigned_once_per_food(self):
    """
    It must not be possible to assign a specific nutrition more
    than once to the same food.
    """
    f = Food(name="Club Mate")
    f.save()

    n1 = Nutrition.objects.create(name="fat")
    n2 = Nutrition.objects.create(name="carbohydrate")
    n1.save()
    n2.save()
    
    c = Composition(food=f, nutrition=n1, ammount_per_100g=20)
    c.save()

    c = Composition(food=f, nutrition=n2, ammount_per_100g=20)
    c.save()

    c = Composition(food=f, nutrition=n1, ammount_per_100g=20)
    with self.assertRaises(IntegrityError):
      c.save()

