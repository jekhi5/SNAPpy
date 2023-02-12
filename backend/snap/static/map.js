// sends the current shopping list 
let sendLocation = () => {
    // disable the button until the list is altered.
    document.getElementById('submit').onclick = "";

    const address = document.getElementById("address");
    const radius = document.getElementById("radius");
    

    var settings = {
        "url": "",
        "method": "POST",
        "timeout": -1,
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
            "zipcode": JSON.stringify(address),
            "radius": JSON.stringify(radius)
        }
    };


      
    $.ajax(settings).done(function (response) {
        // IN THE FUTURE, CLEAR HTML AND DISPLAY THE INFORMATION ON PAGE
        console.log(response);
    });
}
