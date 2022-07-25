// import {Component} from 'react'

// class Something extends Component {

//     componentDidMount() {
//         console.log("I'm alive")
//     }

//     componentDidUpdate() {
//         console.log("I am updating")
//     }

//     componentWillUnmount() {
//         console.log("I am dying")
//     }

//     render() {

//         return(
//             <div>
//                 This is something, The value is {this.props.someValue}
//             </div>
//         )
//     }
// }

import {useEffect, useRef} from "react"


function Something(props){

    let firstRender = useRef(true)

    useEffect( () => {   // on update
        if (!firstRender.current){
            console.log("I'm updating ", props.someValue)
        }
        
    } , [props.someValue])
    
    useEffect(
    () => {
        console.log("I'm alive")
        firstRender.current= false

        return () =>{
            console.log("i'm dying")
        }

    }, [])

    return(
        <div>
            This is something {props.someValue}
        </div>
    )

}


export default Something