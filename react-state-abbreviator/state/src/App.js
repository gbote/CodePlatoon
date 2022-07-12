import './App.css';
import { useState } from "react";

// components
import StateDropDown from './components/StateDropDown';
import StateAbbrDisplay from './components/StateAbbrDisplay';

function App() {
  // states
  const [stateAbbr, setStateAbbr] = useState("");

  // render
  return (
    <div className="App">
      <h2>State Abbreviation App</h2> 
      <hr />
      <StateDropDown setStateAbbr={ setStateAbbr }/>
      <StateAbbrDisplay abbr={ stateAbbr } />
    </div>
  );
}

export default App;