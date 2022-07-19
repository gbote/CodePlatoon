function WordForm(props) {
  // render
  const renderInputs = () => {
    return props.words.map((word, index) => {
        return <input key={index} placeholder={word.label} onChange={(evt) => props.updateMadLibWord(index, evt.target.value)} />
      })
    }
    
// Words come from the MadLibs.jsx. I need to name my element, "word", and "index" to this map.
// I want this map to return an input with a placeholder label. When there is an input change it will go to the index of that
// placeholder and change the space into the new value or evt.target.value

// This will change when the useState() changes from the updateMadLibWord
  
  return (
    <div id="div-words">
      { renderInputs() }
    </div>
  )
}

export default WordForm
