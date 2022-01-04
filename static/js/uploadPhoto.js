"use strict"


document.querySelector("#file").addEventListener("change", (event) => {
    const fileObject = event.target.files
    const result = fileObject[0].name
    document.querySelector("#file-chosen").textContent = result
})