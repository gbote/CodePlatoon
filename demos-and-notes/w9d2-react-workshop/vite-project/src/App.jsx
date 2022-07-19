import React,  { useState } from "react";
import GoodByeWorld from "./GoodByeWorld";
import HelloWorld from "./HelloWorld";
import CurrentTime from "./CurrentTime";
import ChangeWeather from "./ChangeWeather";

function App(props) {
  const [weather, setWeather] = useState('sunny')

  // flips weather from 'sunny' to 'cloudy'
  function updateWeather() {
      if (weather === 'sunny') {
          setWeather('cloudy')
      } else {
          setWeather('sunny')
      }
  }


  const description = "Very"

  return (
    <div>
      <CurrentTime/>
      <HelloWorld 
        weather={weather} 
        prefix={description} 
      />
      <GoodByeWorld 
        weather={weather} 
        prefix={description} 
      />
      <ChangeWeather updateWeather={updateWeather} />
    </div>
  );
}

export default App
