from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils import timezone

from .models import Meal, Meal, Food, Nutrition, Composition
from .models import Packages, ContainerType

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

    c = Composition(food=f, nutrition=n1, ammount_per_100_units=20)
    c.save()

    c = Composition(food=f, nutrition=n2, ammount_per_100_units=20)
    c.save()

    c = Composition(food=f, nutrition=n1, ammount_per_100_units=20)
    with self.assertRaises(IntegrityError):
      c.save()

  def test_if_total_nutritions_are_calculated_correctly(self):
    """
    The formular for the total nutritions is:
    num_packages * calories_per_g_of_nutrition *
    nutrition_ammount_in_food_per_100g *
    ammount per package / 100
    """

    n_fat = Nutrition()
    n_fat.name = "fat"
    n_fat.calories_per_g = 9
    n_fat.save()

    n_carbs = Nutrition()
    n_carbs.name = "carbs"
    n_carbs.calories_per_g = 4
    n_carbs.save()

    n_proteins = Nutrition()
    n_proteins.name = "proteins"
    n_proteins.calories_per_g = 4
    n_proteins.save()

    f = Food()
    f.name = "Ben & Jerrys Cookie Dough"
    f.save()

    c_fat = Composition()
    c_fat.nutrition = n_fat
    c_fat.food = f
    c_fat.ammount_per_100_units = 13.0
    c_fat.save()

    c_carbs = Composition()
    c_carbs.nutrition = n_carbs
    c_carbs.food = f
    c_carbs.ammount_per_100_units = 27.0
    c_carbs.save()

    c_proteins = Composition()
    c_proteins.nutrition = n_proteins
    c_proteins.food = f
    c_proteins.ammount_per_100_units = 3.0
    c_proteins.save()

    f.composition_set.add(c_fat, c_carbs, c_proteins)
    f.save()

    small_container = ContainerType()
    small_container.name = "Small Bucket"
    small_container.save()

    big_container = ContainerType()
    big_container.name = "Big Bucket"
    big_container.save()

    package_small = Packages()
    package_small.container_types = small_container
    package_small.food = f
    package_small.ammount_units = 150.0
    package_small.save()

    package_big = Packages()
    package_big.container_types = big_container
    package_big.food = f
    package_big.ammount_units = 500.0
    package_big.save()

    m_small = Meal()
    m_small.date = timezone.now()
    m_small.food = f
    m_small.packages = package_small
    m_small.ammount = 3
    m_small.save()

    m_big = Meal()
    m_big.date = timezone.now()
    m_big.food = f
    m_big.packages = package_big
    m_big.ammount = 2
    m_big.save()

    # Now check if calculated nutritions are correct

    # Test 1 - Small Bucket:
    d = m_small.kcals_of_nutritions()
    self.assertEqual(d["fat"], 526)
    self.assertEqual(d["carbs"], 486)
    self.assertEqual(d["proteins"], 54)
    self.assertEqual(m_small.kcal_total(), 1066)

    # Test 2 - Big Bucket:
    d = m_big.kcals_of_nutritions()
    self.assertEqual(d["fat"], 1170)
    self.assertEqual(d["carbs"], 1080)
    self.assertEqual(d["proteins"], 120)
    self.assertEqual(m_big.kcal_total(), 2370)

