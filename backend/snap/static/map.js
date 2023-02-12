// sends the current shopping list 
let sendLocation = () => {
    // disable the button until the list is altered.
    // document.getElementById('submit').onclick = "";
    console.log("SEND LOCATION");
    const address = document.getElementById("address").value;
    const radius = document.getElementById("radius").value;
    

    var settings = {
        "url": "",
        "method": "POST",
        "timeout": -1,
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
            "address": JSON.stringify(address),
            "radius": JSON.stringify(radius)
        }
    };

      
    $.ajax(settings).done(function (response) {
        // Hide the elements that are currently on the page
        
        if (response.results.length == 0) {
            const error_div = document.getElementById("result");
            const error_para = document.createElement("p");
            const error_text = document.createTextNode("Error Parsing address or radius. Please be sure \
            your address is formatted properly, and that you've entered a valid mile radius.");
            error_para.appendChild(error_text);
            error_div.appendChild(error_para);
            return;
        }
        
        document.getElementById("address").style.display = "none";
        document.getElementById("radius").style.display = "none";
        document.getElementById("submit").style.display = "none";

        const result_div = document.getElementById("result");
        const map_div = document.getElementById("map");
        const list_div = document.getElementById("list");

        
    });
}

class Supermarket {
            constructor(
                name,
                address,
                storeURL,
                googleURL,
                phone,
                hours,
                is_wheelchair_accessible,
                has_delivery,
                has_curbside_pickup,
                ) {
                this.name = name;
                this.address = address;
                this.storeURL = storeURL;
                this.googleURL = googleURL;
                this.phone = phone;
                this.hours = hours;
                this.is_wheelchair_accessible = is_wheelchair_accessible;
                this.has_delivery = has_delivery;
                this.has_curbside_pickup = has_curbside_pickup;
            }
            
    
    toHTML(parent) {
        const name_para = document.createElement("p");
        const name_text = document.createTextNode(this.name);
        name_para.appendChild(name_text);
        parent.appendChild(name_para);

        const address_para = document.createElement("p");
        const address_text = document.createTextNode(this.address);
        address_para.appendChild(address_text);
        parent.appendChild(address_para);

        const storeURL_para = document.createElement("p");
        const storeURL_text = document.createTextNode(this.storeURL);
        storeURL_para.appendChild(storeURL_text);
        parent.appendChild(storeURL_para);

        const googleURL_para = document.createElement("p");
        const googleURL_text = document.createTextNode(this.googleURL);
        googleURL_para.appendChild(googleURL_text);
        parent.appendChild(googleURL_para);

        const phone_para = document.createElement("p");
        const phone_text = document.createTextNode(this.phone);
        phone_para.appendChild(phone_text);
        parent.appendChild(phone_para);

        const hours_para = document.createElement("p");
        const hours_text = document.createTextNode(this.hours);
        hours_para.appendChild(hours_text);
        parent.appendChild(hours_para);

        const is_wheelchair_accessible_img = document.createElement("img");
        is_wheelchair_accessible_img.src = "/backend/snap/images/HandicapAccessible.png";
        is_wheelchair_accessible_img.setAttribute("height", "50");
        is_wheelchair_accessible_img.setAttribute("width", "50");
        elem.setAttribute("alt", "Is Wheelchair Accessible");
        parent.appendChild(is_wheelchair_accessible_img);

        const has_delivery_img = document.createElement("img");
        has_delivery_img.src = "/backend/snap/images/DeliveryAvailable.png";
        has_delivery_img.setAttribute("height", "50");
        has_delivery_img.setAttribute("width", "50");
        elem.setAttribute("alt", "Has Delivery");
        parent.appendChild(has_delivery_img);

        const has_curbside_pickup_img = document.createElement("img");
        has_curbside_pickup_img.src = "/backend/snap/images/CurbidePickupAvailable.png";
        has_curbside_pickup_img.setAttribute("height", "50");
        has_curbside_pickup_img.setAttribute("width", "50");
        elem.setAttribute("alt", "Has Curbside Pickup");
        parent.appendChild(has_curbside_pickup_img);
    }
}