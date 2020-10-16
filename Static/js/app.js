console.log("This is app.js");

var button = d3.select("#pick-your-org");

function handleClick() {
    console.log("a button was clicked");

    console.log(d3.event.target);
}

button.on("click", handleClick);