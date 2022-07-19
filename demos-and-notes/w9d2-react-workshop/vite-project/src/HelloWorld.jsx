import React from "react";
import CurrentTime from "./CurrentTime";

function HelloWorld(props) {
    if(props.weather === 'sunny') {
        return (
            <div>
                <h1 className="my-class">Hello, world! The weather is {props.prefix} {props.weather}</h1>
                <CurrentTime/>
            </div>
        )
    }

    else {
        return (
            <div>Boo - not sunny</div>
        )
    }
}

// Another way to do the same thing as above.
// Not how we want to do things, only done to demonstrate React.createElement
const helloElement = React.createElement(
  'h2',
  {className: 'greeting'},
  'Hello, World, Again!'
);

export default HelloWorld;