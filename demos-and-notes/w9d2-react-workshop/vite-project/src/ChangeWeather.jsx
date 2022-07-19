import React from "react";

function ChangeWeather(props) {
    const { updateWeather } = props;

    return (
        <button onClick={updateWeather}>CHANGE WEATHER</button>
    )
}

export default ChangeWeather;