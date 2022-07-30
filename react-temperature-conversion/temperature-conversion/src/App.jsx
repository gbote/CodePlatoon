import './App.css';
import { useState, useEffect } from 'react';


// components
import ErrorDisplay from './components/ErrorDisplay';
import InputZipCode from './components/InputZipCode';
import TemperatureDisplay from './components/TemperatureDisplay';

// API KEY
const myOpenWeatherApiKey = "e95cfed0e5e45576733215845f2bfa4d" /* <-- replace with your api key here (using https://home.openweathermap.org/api_keys)*/

function App(){
  // states
  let [temperature, setTemperature] = useState(null)
  let [zipCode, setZipCode] = useState("")

  // effects
  const getTemperature = async ()=> {
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

  useEffect(()=>{
    getTemperature()
  }, [zipCode])

  // handlers
  let updateZipCode = (newZipCode) => {
    setZipCode(newZipCode)
  }

  // render
  const renderDisplay = ()=> {
    // don't show any display if no zip code has been entered
    if (!zipCode) {
      return null
    }
    // show an error if we don't get back valid data
    else if (!temperature) {
      return <ErrorDisplay message="Unable to get temperature information from your zip code." />
    }

    return (
      <div className="App">
        <TemperatureDisplay tempInKelvin={temperature}/>
      </div>
    )
  }

  return (
    <div className="App">
      <h2>Temperature Conversion App</h2>
      <InputZipCode updateZipCode={updateZipCode} buttonText="Get Temperature"/>
      { renderDisplay() }
    </div>
  );
}

export default App;