function IncorrectGuesses(props) {


  console.log("list items: ", document.querySelectorAll(".list-item").length)

  return (
    <div className="incorrect-guesses">
      {props.guessedLetters.length > 0 &&
        <div className="incorrect-guesses__container">
        <h3 className="incorrect-guesses__head">Incorrect Guesses:</h3>
        <ol id="list" className="incorrect-guesses__list">
        {props.guessedLetters.length > 0 && props.guessedLetters.map((letter) => (
        props.puzzle.split('').includes(letter) ? null : <li className="list-item" key={letter}>{letter}</li>
      ))
  }
        </ol>
      </div>
  }
    </div>
  )
}

export default IncorrectGuesses