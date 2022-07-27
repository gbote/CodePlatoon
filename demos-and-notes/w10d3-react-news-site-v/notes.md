# News Site V

## Hooks:
Hooks are functions that let you “hook into” React state and lifecycle features from function components. 

## useState()
A hook that allows you to give a component mutable state variables that can be used throughout the component while it is. 


### useState() syntax
```js

const [user, setUser] = useState({ 'first': 'something', 'last': 'someone'})
const [count, setCount] = useState(0)

```

## useEffect()
The Effect Hook, useEffect, adds the ability to perform side effects from a function component. 

It serves the same purpose as componentDidMount, componentDidUpdate, and componentWillUnmount in React classes, but unified into a single API.


### useEffect() syntax
```js

 // will run every time component renders OR re-renders  equivalent to `componentDidUpdate` 
useEffect( ()=>{       
    
    // -- YOU DON'T WANT TO DO THIS--
    //api call
    //setState  ==> will trigger update again (WATCH OUT FOR THIS WILL CAUSE INFINITE LOOP)
    //-------------------------------

} )     

// will run on mount, it will run once
useEffect( ()=>{  

}, [] ) 

 // will run on mount and unmount
useEffect( ()=>{ 
    // stuff in here will run on mount

    return ()=>{
        // whatever is in here will only run on unmount
    }
}, [] ) 

// will run on mount and update of `stateInstance`
useEffect( ()=>{  
    
    //setDifferentStateInstance() // wont cause re-render or infinite loop 
}, [stateInstance] ) 

```


---- 
code to have update effects separate from on mount
```js
// const firstRender = useRef(true)
    const [firstRenderState, setfirstRenderState] = useState(true)
    const [shouldIUpdate, setShouldIUpdate] = useState(false)

    useEffect( ()=> {
      if (! firstRenderState){
        console.log('The state shouldIUpdate has been updated')
        // other code
      }
      
    } , [shouldIUpdate])

    useEffect( ()=> {
      console.log('this is my first render')
      setfirstRenderState(false)
      // firstRender.current = false
    } , [])



    <button onClick={()=>{setShouldIUpdate(!shouldIUpdate)}}>update</button>
```