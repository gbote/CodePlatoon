import { useState } from "react";
import IncrementButton from "./IncrementButton"
import ResetButton from "./ResetButton";
import OutputLabel from "./OutputLabel";

function ButtonCounter(props) {

    const [counter, setCounter] = useState(0)

    const incrementCounter = () => {
   
        setCounter(prevCounter => prevCounter +1)
     
    }

    const resetCounter = () => {
        setCounter(0)
    }
    return (
        <div>
            <IncrementButton clickFunction = {incrementCounter} />
            <ResetButton handleClick={resetCounter}/>
            <OutputLabel value={counter}/>
        </div>
    )

}

export default ButtonCounter