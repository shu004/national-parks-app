"use strict"


function Welcome(props) {
    let message = "";
    let time = new Date().getHours()

    if (time > 0 && time <= 12) {
        message = `Good morning, ${props.name}`
    } else if (time > 12 && time <= 18) {
        message = `Good afternoon, ${props.name}`
    } else {
        message = `Goodnight, ${props.name}`
    }
    return <h1 className="welcome-message">{message}</h1>
}

let names = document.getElementById("hidden-name").value
names = names.charAt(0).toUpperCase() + names.slice(1)
ReactDOM.render(<Welcome name={names} />, document.querySelector("#root"))