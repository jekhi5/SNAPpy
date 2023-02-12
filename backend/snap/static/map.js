// Handle the keypress into the zipcode field
$('.equipCatValidation').on('keyup keydown change', function(e){
        if ($(this).val() > 9999 
            && e.keyCode !== 46
            && e.keyCode !== 8
           ) {
           e.preventDefault();     
        }
});
    
// sends the current shopping list 
let sendLocation = () => {
    // disable the button until the list is altered.
    document.getElementById('submit').onclick = "";

    const zipcode = document.getElementById("zcode");
    const radius = document.getElementById("radius");
    

    var settings = {
        "url": "",
        "method": "POST",
        "timeout": -1,
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
            "zipcode": JSON.stringify(zipcode),
            "radius": JSON.stringify(radius)
        }
    };


      
    $.ajax(settings).done(function (response) {
        // IN THE FUTURE, CLEAR HTML AND DISPLAY THE INFORMATION ON PAGE
        console.log(response);
    });
}
