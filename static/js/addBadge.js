'use strict'
// post request from frontend posting this to my user saved park table in db
const addBadge = (event) => {
    event.preventDefault();
    //disable the button when user clicked on it
    event.target.disabled = true;

    const formInput = {
        username: document.querySelector('#hidden-username').value,
        parkId: document.querySelector(".park-details-container").id
    };

    fetch('/add-badge', {
        method: 'POST',
        body: JSON.stringify(formInput),
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(responseJson => {
            alert(responseJson.status);
            //if we didn't get the right status, then we want to keep showing the button
            if (!(responseJson.status)) {
                event.target.disabled = false;
            }
        });
}

document.getElementById("add-badge").addEventListener("click", addBadge);

