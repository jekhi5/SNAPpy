// Handle the keypress into the zipcode field
$('.equipCatValidation').on('keyup keydown change', function(e){
        if ($(this).val() > 9999 
            && e.keyCode !== 46
            && e.keyCode !== 8
           ) {
           e.preventDefault();     
        }
    });