document.getElementById("pokedex-number-form").addEventListener("submit", (event) => {
    event.preventDefault();
    pokedexNo = parseInt(document.getElementById("pokedex-number").value);
    boxNumber = Math.ceil(pokedexNo / 30);

    for(var i = 0; i < 5; i++) {
        for(var j = 0; j < 6; j++) {
            document.querySelectorAll("tr")[i].querySelectorAll("td")[j].style.background = "transparent";
        }
    }

    cellNumber = pokedexNo % 30;
    if(cellNumber == 0) {
        cellNumber = 30;
    }

    var counter = 0;
    for(var i = 0; i < 5; i++) {
        for(var j = 0; j < 6; j++) {
            counter++;
            if(counter == cellNumber) {
                document.querySelectorAll("tr")[i].querySelectorAll("td")[j].style.background = "goldenrod";
            }
        }
    }

    document.getElementById("box-number").innerHTML = boxNumber;
});