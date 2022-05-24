// we need a way to get user input
// we need to analyze the input and react appropriately
// - say nothing
// - lower case
// - goodbye (first and second)
// - normal question (all caps)


function deafGrandma() {

    let goodbyeCounter = 0
    let input = ""
    let response = ""
    
    // grandma starts conversation
    console.log("HEY, KID!")
    while (goodbyeCounter <= 1) { // continue talking to grandma so long as we haven't said goodbye more than once
      input = window.prompt("Respond to grandma:", "hello")
      // - say nothing
      if (input === "") {
        response = "WHAT?!"
      // - lower case
      } else if (input !== input.toUpperCase()) {
        response = "SPEAK UP, KID!"
      // - normal question (all caps)
      } else if (input === "GOODBYE!") {
        goodbyeCounter = goodbyeCounter + 1
        if (goodbyeCounter > 1) { // we've said goodbye once before
          response = "LATER, SKATER!"
        } else { // this is the first time we're saying goodbye
          response = "LEAVING SO SOON?"
        }
      } else {
        response = "NO, NOT SINCE 1946!"
      }
      console.log(response)
    }
  }
  
  deafGrandma();