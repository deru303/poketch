from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pokemon, RegionalFormPokemon
from .forms import UpdatePokemonOwnership
from .logic.statistics import calculate_regional_forms_stats, calculate_pokedex_stats
from .logic.pokemon_modify import pokemon_modify

# Create your views here.

def index(response):
    generations = {pkmn.generation for pkmn in Pokemon.objects.all()}
    pokedex = {gen: Pokemon.objects.filter(generation=gen) for gen in generations}
    return render(response, "poketch_app/global_pokedex.html", {"pokedex": pokedex, "active_tab": 1})

def regional_forms(response):
    rforms = RegionalFormPokemon.objects
    generations = {pkmn.generation for pkmn in rforms.all()}
    reg_forms = {gen: rforms.filter(generation=gen) for gen in generations}
    return render(response, "poketch_app/regional_forms.html", {"active_tab": 2, "regional_forms": reg_forms})

def box_utility(response):
    return render(response, "poketch_app/box_utility.html", {"active_tab": 3})

def modify_pokemon(response):
    if response.method == "POST":
        return pokemon_modify(response)
    else:
        return redirect("/")

def statistics(response):
    args = {"active_tab": 4, "global_ownership": calculate_pokedex_stats(), "regional_ownership": calculate_regional_forms_stats()}
    return render(response, "poketch_app/statistics.html", args)
