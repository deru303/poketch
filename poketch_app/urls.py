from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("regional-forms/", views.regional_forms, name="regional_forms"),
    path("box-utility/", views.box_utility, name="box_utility"),
    path("modify-pokemon/", views.modify_pokemon, name="modify_pokemon"),
    path("statistics/", views.statistics, name="statistics")
]