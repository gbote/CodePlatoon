import './App.css';
import { useState, useEffect, useRef } from "react"

// components
import ErrorDisplay from './components/ErrorDisplay.jsx';
import InputZipCode from './components/InputZipCode.jsx';
import TemperatureDisplay from './components/TemperatureDisplay.jsx';

// API KEY
const myOpenWeatherApiKey = "e95cfed0e5e45576733215845f2bfa4d"

function App() {
  
  const [temperature, setTemperature] = useState(null)
  const [zipCode, setZipCode ] = useState('')

  const notFirstRender = useRef(false)
  
  useEffect(() => {
    if (notFirstRender.current) {
      getTemperature()
    } else {
      notFirstRender.current = true
    }
  })

  const getTemperature = async () => {
    try {
      console.log("obtaining temperature...")
      let response = await fetch(`https://api.openweathermap.org/data/2.5/weather?zip=${zipCode},us&appid=${myOpenWeatherApiKey}`)
      
      if (response.ok) {
        let data = await response.json()
        if (data) {
          setTemperature(data.main.temp)
        }
      }
      else {
        setTemperature(null)
      }
    }
    catch (e) {
      console.error(e)
    }
  }

  const updateZipCode = (newZipCode) => {
    setZipCode(newZipCode)
  }

  const renderDisplay = () => {
    // don't show any display if no zip code has been entered
    if (!zipCode) return null
    // show an error if we don't get back valid data
    else if (!temperature) {
      return <ErrorDisplay message="Unable to get temperature information from your zip code." />
    } else {
      return (
        <TemperatureDisplay tempInKelvin={temperature}/>
      )
    }
  }

  return (
    <div className="App">
    <h2>Temperature Conversion App</h2>
    <InputZipCode updateZipCode={updateZipCode} buttonText="Get Temperature"/>
    { renderDisplay() }
  </div>
  )
}

export default App;