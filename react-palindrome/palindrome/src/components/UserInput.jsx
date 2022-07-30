function UserInput(props){

  const changeHandler = () => {
    let inputElement = document.getElementById("input")
    if(inputElement) {
      let userWord = inputElement.value
      props.onSubmitWord(userWord)
    }
  }
  
  return (
    <div>
      <input id="input" type= "text" placeholder='Enter a Word' onChange = { changeHandler } ></input>

    </div>
  )
}

export default UserInput