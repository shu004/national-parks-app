'user strict';

const dropDown = document.querySelector(".navbar .dropdown-menu.form-wrapper");
dropDown.addEventListener("click", function(e) {
    e.stopPropagation();
})