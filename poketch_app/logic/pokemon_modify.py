from django.shortcuts import redirect
from django.http import HttpResponse
from poketch_app.models import Pokemon, RegionalFormPokemon

def pokemon_modify(response):
    if response.POST["pkmn-update-type"] == "regional-forms":
        obj = RegionalFormPokemon.objects.filter(form_number=response.POST["pkmn-pkdex-no"])
    else:
        obj = Pokemon.objects.filter(pokemon_number=response.POST["pkmn-pkdex-no"])

    obj.update(console_owned=response.POST["pkmn-console-owned"])
    obj.update(note=response.POST["pkmn-note"])
    return redirect(response.POST["pkmn-redirect-url"])