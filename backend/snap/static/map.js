const WHEELCHAIR_EMOJI = "♿";
const DELIVERY_VEHICLE = "🚗";
const CURBSIDE_PICKUP_PERON = "🧍";

// sends the current shopping list 
let sendLocation = () => {
    // disable the button until the list is altered.
    // document.getElementById('submit').onclick = "";

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
            const error_div = document.getElementById("results");
            const error_para = document.createElement("p");
            const error_text = document.createTextNode("Error Parsing address or radius. Please be sure \
            your address is formatted properly, and that you've entered a valid mile radius.");
            error_para.appendChild(error_text);
            error_div.appendChild(error_para);
            return;
        }
        
        // document.getElementById("address").style.display = "none";
        // document.getElementById("radius").style.display = "none";
        // document.getElementById("address_label").style.display = "none";
        // document.getElementById("radius_label").style.display = "none";
        // document.getElementById("submit").style.display = "none";

        const result_div = document.getElementById("results");
        const map_div = document.getElementById("map");
        const supermarket_list_div = document.getElementById("supermarket_list");

        const mapped = response.results.map(function (elem, i, arr) {
            return {"supermarket_object": new Supermarket(
                elem.name,
                elem.vicinity,
                elem.website,
                elem.url,
                elem.formatted_phone_number,
                [elem.current_opening_hours.periods[0].open.time,
                elem.current_opening_hours.periods[0].close.time],
                elem.is_wheelchair_accessible_entrance,
                elem.delivery,
                elem.has_curbside_pickup),
                "latlng": elem.latlng};
        }, this);

        mapped.forEach(function (elem, i, arr) {
            console.log(elem)
            const obj = elem.supermarket_object;
            obj.toHTML(supermarket_list_div);
        }, this);
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
                is_wheelchair_accessible=false,
                has_delivery=false,
                has_curbside_pickup=false,
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

        const name_text = document.createElement("a");
        name_text.setAttribute("class", "data");
        name_text.setAttribute("href", this.storeURL);
        name_text.innerHTML = this.name;

        const address_text = document.createElement("a");
        address_text.setAttribute("class", "data");
        address_text.setAttribute("href", this.googleURL);
        address_text.innerHTML = this.address;

        const storeURL_para = document.createElement("p");
        storeURL_para.setAttribute("class", "data");
        const storeURL_text = document.createTextNode(this.storeURL);
        storeURL_para.appendChild(storeURL_text);

        const googleURL_para = document.createElement("p");
        googleURL_para.setAttribute("class", "data");
        const googleURL_text = document.createTextNode(this.googleURL);
        googleURL_para.appendChild(googleURL_text);

        const phone_para = document.createElement("p");
        phone_para.setAttribute("class", "data");
        const phone_text = document.createTextNode(this.phone);
        phone_para.appendChild(phone_text);

        const hours_para = document.createElement("p");
        hours_para.setAttribute("class", "data");
        const opening_hours = this.hours[0].substring(0, 2) + ":" + this.hours[0].substring(2);
        const closing_hours = this.hours[1].substring(0, 2) + ":" + this.hours[1].substring(2);
        const hours_text = document.createTextNode(opening_hours + " - " + closing_hours);
        hours_para.appendChild(hours_text);


        const data_container = document.createElement("div");
        data_container.setAttribute("class", "data_container");
        data_container.appendChild(name_text);
        data_container.appendChild(address_text);
        data_container.appendChild(storeURL_para);
        data_container.appendChild(googleURL_para);
        data_container.appendChild(phone_para);
        data_container.appendChild(hours_para);



        const is_wheelchair_accessible_para = document.createElement("p");
        const is_wheelchair_accessible_emoji = document.createTextNode(WHEELCHAIR_EMOJI);
        is_wheelchair_accessible_para.setAttribute("class", "icon");
        is_wheelchair_accessible_para.appendChild(is_wheelchair_accessible_emoji);
        parent.appendChild(is_wheelchair_accessible_para);

        const has_delivery_para = document.createElement("p");
        const has_delivery_emoji = document.createTextNode(DELIVERY_VEHICLE);
        has_delivery_para.setAttribute("class", "icon");
        has_delivery_para.appendChild(has_delivery_emoji);
        parent.appendChild(has_delivery_para);

        const has_curbside_pickup_para = document.createElement("p");
        const has_curbside_pickup_emoji = document.createTextNode(CURBSIDE_PICKUP_PERON);
        has_curbside_pickup_para.setAttribute("class", "icon");
        has_curbside_pickup_para.appendChild(has_curbside_pickup_emoji);
        parent.appendChild(has_curbside_pickup_para);


        const icon_container = document.createElement("div");
        icon_container.setAttribute("class", "icon_container");
        icon_container.appendChild(is_wheelchair_accessible_para);
        icon_container.appendChild(has_delivery_para);
        icon_container.appendChild(has_curbside_pickup_para);

        
        
        const result_container = document.createElement("div");
        result_container.setAttribute("class", "supermarket_box");
        result_container.appendChild(data_container);
        result_container.appendChild(icon_container);



        parent.appendChild(result_container);
    }
}