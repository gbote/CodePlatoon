function Input(props) {

  const onSubmit = () => {
    let inputEl = document.getElementById("userInput")
    if (inputEl) {
      console.log("inputEl: ", inputEl)
      let guess = inputEl.value.toLowerCase()
      console.log("guess: ", guess)
      if (guess.length > 1 || guess == "") {
        alert("You must guess one letter at a time.")
      } else if (guess.match(/[^a-z]/i)) {
        alert("Your guess must be a letter.")
      }
      else if (props.guessedLetters.includes(guess)) {
        alert(`Try again! You have already guessed the letter "${guess}".`)
      } else {
        props.setGuessedLetters([...props.guessedLetters, guess])
        console.log("guessed: ", props.guessedLetters)  
      }
      inputEl.value=""
    }
    props.checkIfLost()
  }

  const keyPress = (e) => {
    if (e.keyCode == 13) {
      console.log("pressed enter")
      onSubmit()
    }
  }

  return (
    <div className="input__container">
      <input id="userInput" type="text" placeholder="Enter a letter here" required onKeyDown={keyPress} />
      <button className="btn primary" onClick={onSubmit}>Guess</button>
    </div>
  )
}

export default Input