const inputIdStr = "input-word"

function WordInput(props) {
  // event handler
  const clickHandler = () => {
    let inputElement = document.getElementById(inputIdStr)
    if (inputElement) {
      // extract user value
      let userWord = inputElement.value

      // call prop function (to notify parent component)
      props.functionToCallWhenButtonIsClicked(userWord)

      // clear input
      inputElement.value = ""
    }
  }

  // render
  return (
    <div>
      <input id={inputIdStr} type="text" placeholder="enter a word" />
      <button onClick={ clickHandler }>Submit Word</button>
    </div>
  )
}

export default WordInput;