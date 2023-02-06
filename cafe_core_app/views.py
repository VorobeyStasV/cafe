from django.shortcuts import render
from .models import Meal
from django.utils import timezone

import matplotlib.pyplot as plt

def menu(request):
    meal_categories = list(filter(lambda el: 'NO_TYPE' not in el[0], Meal.MealType.choices))
    return render(request, 'cafe_core_app/menu.html', {'meal_categories': meal_categories})


#наши блюда
def meal_category(request, meal_category):
      meals_by_category = Meal.objects.filter(meal_type=meal_category)
      return render(request, 'cafe_core_app/meals.html', {'meals': meals_by_category, 'meal_category': meal_category})


#click по нашим meal
def meal(request, meal_id):
      meal = Meal.objects.get(id=meal_id)
      meal.mealclick_set.create(click_date=timezone.now())
      return render(request, 'cafe_core_app/meal.html', {'meal': meal})


# class meal_statistics(request):
#      click = MealClick.objects.all()
#
#      food = []
#      for i in click:
#          food.append(i.meal.name)
#
#      pes = {}
#      pes_ = {}
#
#      for name in food:
#          pes[name] = pes.get(name, 0) + 1
#      for i, x in sorted(sorted(pes.items()), key=lambda x: x[1], reverse=True):
#          if not len(pes_) == 3:
#              pes_[i] = pes_.get(i, x)
#
#      names = []
#      for i in users:
#          names.append(i.name)
#
#      res = []
#      res_ = []
#
#      for name in name:
#          pes[name] = pes.get(name, 0) + 1
#      for i, x in sorted(sorted(pes.items()), key=lambda x: x[1], reverse=True):
#          if not len(pes_) == 10:
#              pes_[i] = pes_.get(i, x)
#
#      context = {
#          'value': click,
#          'uesrs': users,
#          'res': res_,
#          'meal': pes_
#      }
#      render(requests, 'meal_statistics.html', context=context)

matplotlib.use('Add')
def GraphsViewBar(request, meal_id):
    namb = 0
    x = []
    y = []
    meal = Meal.objects.get(id=meal_id)

    for i in meal.mealclick_set.all():
        namb += 1
        x.append(namb)
        y.append(i.click_date.strftime("%d-%x-%y"))
    fig = plt.figure()
    plt.plot(x, y)
    plt.show()
    plt.ylabel(meal.name)
    plt.ylabel('Дата')
    os.remove('')
    fig.savefig('')
    addr = ''
    plt.close(fig)
    return render(requests, 'grafic.html', {'addr': addr})