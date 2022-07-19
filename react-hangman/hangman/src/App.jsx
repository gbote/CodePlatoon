import {useEffect, useState} from 'react'
import data from "./data/data"
import Header from './components/Header'
import Input from './components/Input'
import Word from './components/Word'
import IncorrectGuesses from './components/IncorrectGuesses'

import './App.css';

function App() {

  // const randomNumber = () => (
  //   Math.floor(Math.random() * 24)
  // )

  const [puzzle, setPuzzle] = useState('')
  // const [isLoaded, setIsLoaded] = useState(false)
  // const [puzzle, setPuzzle] = useState(data[randomNumber()])
  const [guessedLetters, setGuessedLetters] = useState([])

  useEffect(() => {
    fetch("https://random-word-api.herokuapp.com/word")
    .then(response => response.json())
    .then((result) => {
      console.log("result: ", result)
      setPuzzle(result[0])
      // setIsLoaded(true)
    },
    (error) => {
      console.log("ERROR")
    })
  }, []);


  const checkIfLost = () => {
    let listItemArr = document.querySelectorAll(".list-item")
    if (listItemArr.length >= 6) {
      alert(`Game over! The word was ${puzzle}.`)
      window.location.reload(false);
    }
  }

  return (
    <div className="App">
      <Header />
      <Input guessedLetters={guessedLetters} setGuessedLetters={setGuessedLetters} checkIfLost={checkIfLost}/>
      {puzzle != "" && 
      <Word puzzle={puzzle} guessedLetters={guessedLetters}/> }
      <IncorrectGuesses puzzle={puzzle} guessedLetters={guessedLetters} setGuessedLetters={setGuessedLetters}/>
    </div>
  );
}

export default App;