function InputZipCode(props) {

  const handleZipCode = () => {
    const inputZipCode = document.getElementById("input-zipcode")
    console.log(inputZipCode.value)
    props.updateZipCode(inputZipCode.value)
  }

  return (
    <div>
      <div className="form">
        <input id="input-zipcode" placeholder="Enter zip code"/>
        <button onClick={handleZipCode}>{ props.buttonText }</button>
      </div>
    </div>
  )
}

export default InputZipCode