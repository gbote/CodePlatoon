# React: Detention

There's nothing like old fashioned mental conditioning. In order to emphasize one of the most important rules in React, you will write/render it 100 times:

*"I will never mutate state or props directly"*

This means NOT doing the following:
```javascript
function MyComponent(props) {
  const [myStateValue, setMyStateValue] = useState(0)
  
  myStateValue = 1 // BAD!
  props.myPropValue = true // BAD!
}
```

For functional components, we'll be using the [`useState()`](https://reactjs.org/docs/hooks-state.html) hook. 

## Release 0: Setup
* Use `create-react-app` to scaffold an app

## Release 1: Detention
* Write "I will never mutate state or props directly" 100 times. In other words create a functional component and reuse it 100 times.

## Release 2: Styling
* Research CSS, and attempt to style the page to look like writing on a chalkboard (an idea called `skeuomorphic design`).

Hint: Investigate the Array object's fill and map functions - these will help you in your journey.
