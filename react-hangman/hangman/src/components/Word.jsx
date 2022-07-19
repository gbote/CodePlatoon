function Word(props) {

  console.log("puzzle: ", props.puzzle)
  console.log("guessedletters in Word: ", props.guessedLetters)

  const renderWord = (word, arr) => {
    let lettersArr = word.split('')
    let formattedArr = lettersArr.map((letter) => (
      arr.includes(letter) ? letter : "_ "
    ))
    console.log("formatted: ", formattedArr)
    checkForWin(formattedArr)
    return formattedArr
  }

  const checkForWin = (arr) => {
    if (!arr.includes("_ ")){
      alert(`You won! The word was ${props.puzzle}.`)
      window.location.reload(false);
    }
  }


  return (
    <div className="word__container">
      <p className="word__progress">
        {renderWord(props.puzzle, props.guessedLetters)}
      </p>
  </div>
)
}

export default Word