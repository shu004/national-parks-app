'use strict'


document.getElementById('picture-form').addEventListener("submit", function(event) {
    event.preventDefault()
    //is this the right forminput? we need the fileName to call the API
    const formInput = {
        fileName: document.getElementById('file').value,
        username: document.querySelector('#hidden-username').value
    }

    console.log(`here's the form input ${JSON.stringify(formInput)}`)

    fetch('/post-form-data', {
        method: 'POST',
        body: JSON.stringify(formInput),
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(responseJson => {
            alert(responseJson.status);
        });
});