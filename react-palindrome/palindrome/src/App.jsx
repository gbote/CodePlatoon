import {useState, useEffect} from 'react'
import Header from './components/Header.jsx';
import UserInput from './components/UserInput.jsx';
import Feedback from './components/Feedback.jsx';
import './App.css';

function App() {

  const [word, setWord] = useState('')
  const [delayedWord, setDelayedWord] = useState('')
  const [isPalindrome, setIsPalindrome] = useState(false);

  const cleanConvertoArray = (inputWord) => {
    return typeof(inputWord) === 'string' ? inputWord.toLowerCase().replace(/[^a-z0-9]/ig, "").split("") : inputWord.toString().split('')
  }

  useEffect(() => {

    const checkWord = (inputWord) => {
      return cleanConvertoArray(inputWord).reverse().join() === cleanConvertoArray(inputWord).join() ? setIsPalindrome(true) : setIsPalindrome(false);
    }
  
    const delayFeedback = setTimeout(() => {
      let lowercaseWord = word.toLowerCase()
      setDelayedWord(lowercaseWord)
      checkWord(delayedWord)
    }, 500);
  
    return () => clearTimeout(delayFeedback)
  }, [word, delayedWord, isPalindrome])
  


  return (
    <div className="App">
      <Header />
      <UserInput word={word} setWord={setWord}/>
      <Feedback delayedWord={delayedWord} isPalindrome={isPalindrome} />
    </div>
  );
}

export default App;