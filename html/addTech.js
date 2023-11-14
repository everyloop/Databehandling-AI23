function addTechnology() {
    // Prompt the user for the technology name
    var newTech = prompt("Enter the name of the new technology:");

    if (newTech) {
        // Create a new list item
        var listItem = document.createElement("li");

        // Add the new technology to the list item
        listItem.innerHTML = "<b>" + newTech + ": </b>Some description.";

        // Append the new list item to the existing list
        document.getElementById("techList").appendChild(listItem);
    }
}