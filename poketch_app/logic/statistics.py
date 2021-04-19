from poketch_app.models import Pokemon, RegionalFormPokemon
from django.db.models import Q

def _calculate_stats(data_source, generation_filter_kwargs):
    if generation_filter_kwargs["generation"] == "summary":
        generation_filter_kwargs = dict()

    return (
        data_source.filter(**generation_filter_kwargs).count(),
        data_source.filter(**generation_filter_kwargs).filter(~Q(console_owned="")).count(),
        data_source.filter(**generation_filter_kwargs).filter(console_owned="").count(),
        round(data_source.filter(**generation_filter_kwargs).filter(~Q(console_owned="")).count() / data_source.filter(
            **generation_filter_kwargs).count() * 100, 2),
    )


def calculate_pokedex_stats():
    pkmn = Pokemon.objects
    global_generations = {p.generation for p in pkmn.all()}
    global_generations.add("summary")

    return {
        gen: _calculate_stats(pkmn, dict(generation=gen))
        for gen in global_generations
    }

def calculate_regional_forms_stats():
    rpkmn = RegionalFormPokemon.objects
    regional_generations = {p.generation for p in rpkmn.all()}
    regional_generations.add("summary")

    return {
        gen: _calculate_stats(rpkmn, dict(generation=gen))
        for gen in regional_generations
    }