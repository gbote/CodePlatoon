function IncrementButton (props) {

    return(
        <div>
            <button id='my-button' onClick={props.clickFunction}> Click Me</button>
        </div>
    )

}
export default IncrementButton