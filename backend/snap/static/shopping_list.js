// add a new item to the list
let addItem = () => {
    // re-enable the submit button if it has been disabled
    //document.getElementById('submit').onclick = "sendList()";

    const inputBox = document.getElementById("new-item-name");
    const itemName = inputBox.value;
    inputBox.value = ""
    const shoppingList = document.getElementById("shopping-list");
    let newItem = document.createElement("li");
    newItem.appendChild(document.createTextNode(itemName));
    shoppingList.appendChild(newItem);
}

// return an array of all the item names in the list
let summarize_list = () => {
    const shoppingList = document.getElementById("shopping-list");

    output = [];

    for (let li of shoppingList.childNodes.values()) {
        output.push(li.innerHTML)
    }

    // output needs to be shifted because of the initial TextNode.
    output.shift()
    return output;
}

// sends the current shopping list 
let sendList = () => {
    // disable the button until the list is altered.
    //document.getElementById('submit').onclick = "";

    // Get the current shopping list
    const items = summarize_list();

    // Build the POST request
    var settings = {
        "url": "",
        "method": "POST",
        "timeout": -1,
        "headers": {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": {
          "shoppingList": JSON.stringify(items)
        }
      };
      
      // Send the POST request to the server.
      // The callback function should replace the current page with the map.
      $.ajax(settings).done(function (response) {
        const results = document.getElementById('results');
        
        console.log(response);

        if (response.hits > 0) {
          const link = document.createElement('a');
          link.setAttribute("href", response.url);
          link.innerHTML = response.title;
          results.appendChild(link);
          
        } else {
          const resP = document.createElement('p');
          resP.appendChild(document.createTextNode("No recipes found with your ingredients. Try adding more!"));
          results.appendChild(resP);

        }

        results.appendChild(document.createElement('br'));
      });
}