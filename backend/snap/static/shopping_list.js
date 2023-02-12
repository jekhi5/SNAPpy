// add a new item to the list
let addItem = () => {
    // re-enable the submit button if it has been disabled
    document.getElementById('submit').onclick = "sendList()";

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

    // childNodes needs to be shifted because of the TextNode.
    for (let li of shoppingList.childNodes.values()) {
        output.push(li.innerHTML)
    }

    output.shift()
    return output;
}

// sends the current shopping list 
let sendList = () => {
    // disable the button until the list is altered.
    //document.getElementById('submit').onclick = "";

  const items = summarize_list();

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
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
}