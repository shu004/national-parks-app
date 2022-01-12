/* It checks to see if the span id #heart has "liked" class
if not it run the else statement and adds the "liked" class.
on a 2nd click it see that it has the "liked" class so it replaces the
innerHTML and removes class, on 3rd click it runs the else statement
again cause there is no "liked" class(removed on 2nd click). */


const allHearts = document.querySelectorAll(".heart")


for (const heart of allHearts) {
    const addToFav = (event) => {

        const formInput =  {
            username: document.querySelector('#hidden-username').value,
            trailId: heart.id
        }

        //if they already liked the trail
        if (heart.classList.contains("liked")) {
            heart.innerHTML = ('<i class="fa fa-heart-o" aria-hidden="true"></i>');
            heart.classList.remove("liked");

            fetch('/like-trail/delete', {
                method: 'POST',
                body: JSON.stringify(formInput),
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(responseJson => {
                    // alert(responseJson.status)
                })
        //if they havent
        } else {
            heart.innerHTML = ('<i class="fa fa-heart" aria-hidden="true"></i>');
            heart.classList.add("liked")

            fetch('/like-trail', {
                method: 'POST',
                body: JSON.stringify(formInput),
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(responseJson => {
                    // alert(responseJson.status)
                })
        }
    }

    heart.addEventListener("click", addToFav)
}


