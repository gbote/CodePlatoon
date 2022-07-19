function Story(props) {
  // render
  
  const renderStory = () => {
    return (
      <div>
        <h2>{props.text}</h2>
      </div>
      )
  }

  return (
    <div id="div-story">
      { renderStory() }
    </div>
  )
}

export default Story

// Here, we can render the text from the getText() that can be found from the 
// MadLibs.jsx file.