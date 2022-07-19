function OutputLabel (props) {
    const counter = props.value
    
    const renderOutput = () =>{
        if (counter == 0) {
            return 'You havent clicked the button yet'
        }
        const maxCount = 5
        if (counter > maxCount){
            return `You've clicked the counter morre than ${maxCount} times. `

        }
        return `you've clicked the button ${counter} times`
    }

    return(
        <p id="my-output"> {renderOutput()}</p>
    )
}
export default OutputLabel