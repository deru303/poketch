from django import forms

class UpdatePokemonOwnership(forms.Form):
    pokemon_number = forms.CharField(widget=forms.HiddenInput(), required=True)
    update_type = forms.CharField(widget=forms.HiddenInput(), required=True)
    console_owned = forms.CharField(max_length=255, label="Console owned", required=False)
    tcg_owned = forms.CharField(max_length=255, label="TCG owned", required=False)
