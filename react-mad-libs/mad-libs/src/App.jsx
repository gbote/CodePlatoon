import "./App.css"
import React, { useState } from "react"

// data
import MadLibsData from "./data/MadLibs.jsx"

// components
import Selector from "./components/Selector.jsx"
import Story from "./components/Story.jsx"
import WordForm from "./components/WordForm.jsx"

function App() {

  const [selectedMadLib, setSelectedMadLib] = useState(MadLibsData[0])

  const updateMadLibWord = (wordIndex, wordValue) => {  
    let newSelectedMadLib = { ...selectedMadLib }
  
    newSelectedMadLib.words[wordIndex] = {
      ...newSelectedMadLib.words[wordIndex],
      userWord: wordValue
    }

    setSelectedMadLib(newSelectedMadLib)
  }

  const checkIfAllFieldsFilled = () => {
    return selectedMadLib.words.every((item) => {
      return item.userWord
    })
  }

    const isStoryDone = () => {
      return checkIfAllFieldsFilled()
    }


  return (
    <div className="App">
      <h2>MadLibs!</h2>
      <Selector data={MadLibsData} setSelectedMadLib={setSelectedMadLib} />
      <WordForm words={selectedMadLib.words} updateMadLibWord={updateMadLibWord} />
      {isStoryDone() &&  <Story text={selectedMadLib.getText()} />}
    </div>
  )
}

export default App