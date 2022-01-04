// It checks to see if the span id #heart has "liked" class, i
//if not it run the else statement and adds the "liked" class,
//on a 2nd click it see that it has the "liked" class so it replaces the
//ihherHTML and removes class, on 3rd click it runs the else statement
//again cause there is no "liked" class(remomved on 2nd click).


const allHearts = document.querySelectorAll(".heart")
for (const heart of allHearts) {
    const addToFav = (event) => {
        if (heart.classList.contains("liked")) {
            heart.innerHTML = ('<i class="fa fa-heart-o" aria-hidden="true"></i>');
            heart.classList.remove("liked");
        } else {
            heart.innerHTML = ('<i class="fa fa-heart" aria-hidden="true"></i>');
            heart.classList.add("liked")
        }
    }

    heart.addEventListener("click", addToFav)
}
