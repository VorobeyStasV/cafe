from django.urls import path
from . import views
from rest_framework import routers
# from .api import TodoViewSet

# router = routers.DefaultRouter()
# router.register('api/todo', TodoViewSet, 'todo')
#
# urlpatterns = router.url

app_name = 'cafe_core_app'
urlpatterns =[
    path('', views.menu, name='menu'),
    path('menu', views.menu, name='menu'),
    path('<meal_category>', views.meal_category, name='meal_category'),
    path('<int:meal_id>/meal', views.meal, name='meal'),
    # path('meal_statistics', views.meal_statistics, name='meal_statistics'),
    # path('<int:meal_id>/grafic', views.GraphsViewsBar, name='grafic')
]