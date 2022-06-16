let randomNum = Math.floor(Math.random() * 100) + 1

const tryGuess = () => {
  let guess = document.getElementById("userGuess").value
  let lowfeedback = document.getElementById("lowfeedback")
  let highfeedback = document.getElementById("highfeedback")
  let success = document.getElementById("sucess")
  let newGame = document.getElementById("new-game")
  let newDiv = document.createElement("div")

  console.log(randomNum)
  if (guess == "") {
    newDiv.innerText = "Input not recognized!"
    success.appendChild(newDiv)
  } else if(guess > randomNum){
    newDiv.innerText = `${guess} is too large. Try again by guessing LOWER!`
    lowfeedback.appendChild(newDiv)
  } else if(guess < randomNum) {
    newDiv.innerText = `${guess} is too small. Try again by guessing HIGHER!`
    highfeedback.appendChild(newDiv)
  } else if(guess == randomNum) {
    newDiv.innerText = `${guess} is correct! Good job!`
    success.appendChild(newDiv)
    let newG = document.createElement("div")
    newG.classList.add("d-grid" , "gap-2")
    newG.innerHTML = `<button onClick="window.location.reload();" class="btn btn-primary" type="button">New Game</button>`
    newGame.appendChild(newG)
  } else{
    newDiv.innerText = "Input not recognized!"
    success.appendChild(newDiv)
  }

}