import React, { useState } from "react";

function CurrentTime() {
    const now = new Date().toLocaleString()
    const [time, setTime] = useState(now)

    function updateTime() {
        const now = new Date().toLocaleString();
        setTime(now);
    }

    setInterval(updateTime, 1000)

    return (
        <h4>Current Time is {time}</h4>
    )
}

export default CurrentTime;