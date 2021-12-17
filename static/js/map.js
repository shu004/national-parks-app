'use strict'

function initMap() {
    //getting park_id from the div container in html
    const park_id = document.querySelector(".park-details-container").id

    /*create a queryString because you need to pass park_id to backend db to get specific
    info for that specific park id*/
    const queryString = new URLSearchParams({park_id: park_id})

    fetch(`/getcoords.json?${queryString}`)
        .then(response => response.json())
        .then(jsonData => {

        const basicMap = new google.maps.Map(document.querySelector('#map'), {
            center: jsonData,
            zoom: 8,
        });

        const coordMarker = new google.maps.Marker({
            position: jsonData,
            title: 'Park location',
            map: basicMap,
        });
    })
}