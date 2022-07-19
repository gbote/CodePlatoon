
import React from "react";

function GoodByeWorld(props) {
    // Object deconstruction - does the same thing as the commented-out code below
    const { setWeather, weather, prefix } = props;
//  const setWeather = props.setWeather;
//  const weather = props.weather;
//  const prefix = props.prefix;

  if(weather === 'cloudy') {
    return (
        <div>
            <h1 className="my-class">The darn weather is still {prefix} {weather}. Goodbye, World!</h1>
        </div>
    )
  }

  else {
    return (
        <div>
            <div>Boo! It's not cloudy : (</div>
        </div>
    )
  }
}

export default GoodByeWorld;