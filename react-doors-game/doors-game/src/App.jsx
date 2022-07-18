import './App.css';
import Game from "./components/Game"
import { Component } from 'react'

class App extends Component {


  render() {
    return (
      <div className="App" >
        <Game numDoors={4} />
      </div>
    )
  };
}

export default App;