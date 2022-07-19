import { useEffect, useState } from 'react'

function TemperatureDisplay(props) {

  const [tempInCelsius, setTempInCelsius] = useState()
  const [tempInFahrenheit, setTempInFahrenheit] = useState()

  useEffect(() => {
    const updateTempValues = () => {
      let tC = props.tempInKelvin - 273.15
      let tF = (tC * 9 / 5) + 32
  
      setTempInCelsius(tC.toFixed(2))
      setTempInFahrenheit(tF.toFixed(2))
    }
  
    updateTempValues()
  }, [props.tempInKelvin])



  return (
    <div className='temp-display'>
      <p>Current Temperature:</p>
      <div className="temp-container">
        <span className="temperature">
          { tempInCelsius }
        <span className="units">°C</span>
        </span>
      {/* </div> */}
      {/* <div class="temp-container"> */}
        <span className="temperature">
          { tempInFahrenheit }
        {/* </span> */}
        <span className="units">°F</span>
        </span>
      </div>
    </div>
  )
}

export default TemperatureDisplay;