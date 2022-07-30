import './App.css';
import UserInput from './components/UserInput';
import Output from './components/Output';
import { useState } from "react";

function App() {
  const [word, setWord] = useState("")
  const onSubmitWord = (newWord) => {setWord(newWord)}
  return (
    <div className="App">
      <h1>Palindrome Checker</h1>
      <UserInput onSubmitWord = {onSubmitWord}/>
      <Output word={word}/>
    </div>
  );
}

export default App;