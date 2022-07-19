import { useState } from "react";

function MyComponent(){

    const [myData, setMyData] = useState([5, 4,2])

    const appendData = () => {
        let newNum = Math.floor(Math.random() * 20)
        console.log(newNum)
        let newData = [...myData, newNum]
        setMyData(newData)
    }

    const renderData = () => {
        let elements = []
        for (let i = 0; i < myData.length; i++) {
            elements.push(<li id={`${i}`} key={`${i}`}>{myData[i]}</li>)
        }

        return elements
    }
    return (
        <div>
            <button onClick={appendData}> click me</button>
            <ul>
                {renderData()}
            </ul>
        </div>
    )


}
export default MyComponent