const imgs = document.querySelectorAll('.pokemon-img img');

const onImageClicked = function(event) {
    event.preventDefault();

    let title = document.querySelector("#pokemon-img-modal .modal-title");
    let img = document.querySelector("#pokemon-img-modal img");

    title.innerHTML = event.target.alt;
    img.src = event.target.src;
    img.alt = event.target.alt;

    new bootstrap.Modal(document.querySelector("#pokemon-img-modal")).show();
};

imgs.forEach(el => el.addEventListener('click', onImageClicked));
