import './App.css';

import { useState } from "react"

// components
import MyHeader from "./components/MyHeader.js"
import WordInput from "./components/WordInput.js"
import VowelFinder from './components/VowelFinder.js';

function App() {
  // states
  let [words, setWords] = useState([]); // this function takes in one input, and return a list of two outputs

  // event handler
  const onSubmitWord = (newWord) => {
    setWords([...words, newWord]) // update our 'words' array value via this updating function (so React knows about this update)
    console.log("new word:", newWord)
  };

  // render
  return (
    <div className="App">
      <MyHeader text="My Vowel Finder App"/>
      <hr />
      <WordInput functionToCallWhenButtonIsClicked={onSubmitWord} /> {/* poorly named prop */}
      { words.map((word) => { return <VowelFinder word={word} /> }) }
    </div>
  );
}

export default App;