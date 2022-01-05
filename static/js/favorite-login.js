"use strict";



const heartsLogIn = document.querySelectorAll(".heart")


for (const heart of heartsLogIn) {
    const showAlert = () => {
        alert("Please log in to add to favorite")
    }
    heart.addEventListener("click", showAlert)
}

