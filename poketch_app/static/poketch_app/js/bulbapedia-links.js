const links = document.querySelectorAll('.bulbapedia-link');

const onBulbapediaLinkClicked = function(event) {
    event.preventDefault();

    let iframe = document.querySelector("#bulbapedia-modal iframe");
    iframe.src = event.target.href;

    new bootstrap.Modal(document.querySelector("#bulbapedia-modal")).show();
};

links.forEach(el => el.addEventListener('click', onBulbapediaLinkClicked));
