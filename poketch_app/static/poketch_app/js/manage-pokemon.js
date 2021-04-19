const manageBtns = document.querySelectorAll('.pokemon-manage button');

const onBtnClicked = function(event) {
    event.preventDefault();

    let pkdexNo = event.target.dataset.pokedexNo;
    let pokemon = event.target.parentElement.parentElement;

    let pokemon_console_owned = pokemon.querySelector(".pokemon-console-owned").innerHTML;
    let pokemon_note = pokemon.querySelector(".pokemon-note").innerHTML;

    if (window.location.href.includes("regional-forms")) {
        document.getElementById("pkmn-update-type").value = "regional-forms";
    }
    else {
        document.getElementById("pkmn-update-type").value = "global-pokedex";
    }

    document.getElementById("pkmn-pkdex-no").value = pkdexNo;
    document.getElementById("managed-pokemon").innerHTML = pkdexNo;
    document.getElementById("pkmn-console-owned").value = pokemon_console_owned;
    document.getElementById("pkmn-note").value = pokemon_note;

    document.getElementById("pkmn-redirect-url").value = window.location.href.split("#")[0] + "#pokemon-" + pkdexNo;
    new bootstrap.Modal(document.querySelector("#pokemon-manage-modal")).show();
};

manageBtns.forEach(el => el.addEventListener('click', onBtnClicked));