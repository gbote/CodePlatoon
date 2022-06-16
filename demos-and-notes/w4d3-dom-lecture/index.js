console.log('JS script file being read by browser');

function handleClick(event) {
  event.stopPropagation();
  console.log('INNER CLICK LISTENER')

}

function handleFormSubmit(event) {
  // Prevents form "default behavior" - which is to send data to server
  // and refresh the page.
  event.preventDefault();
  console.log('SUBMITTING');
  
  let evt = event;
  let nameElem = evt.target.elements[0]
  console.log(nameElem.name, nameElem.value)
  let favColorElem = evt.target.elements[1]
  console.log(favColorElem.name, favColorElem.value)
  
}

// When called, gets an <input> with id="input-name"
// and prints anything the user has typed into the <input> element.
function showGreeting(event) {
  console.log("Event Listener A");
  console.log("EVENT: ", event.target.value);
  let nameInput = document.getElementById("input-name");
  // console.log(nameInput);

  let nameInputValue = nameInput.value;
  console.log("Input Value: " + nameInputValue);
}

// Example of adding an event listener for a 'click' event to a button.
// Uncomment the code to see it in action.
/**
document
  .getElementById("my-button")
  .addEventListener("click", (event) => {
    console.log("Event Listener B");
    showGreeting(event);
  });
**/

// Adds a 'click' event listener to an element with id="my-button"
//Uncomment the code to see it in action.
/**
document
  .getElementById("my-button")
  .addEventListener("click", (event) => {
    console.log("Event Listener B");
    console.log("EVENT: ", event.target.value);
  });
**/