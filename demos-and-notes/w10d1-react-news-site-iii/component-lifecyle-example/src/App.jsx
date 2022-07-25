import './App.css'
import {Component} from 'react'
import Something from './something'

class App extends Component{

  state = {
    exists: false,
    someValue: 0
  }

  render() {
    

    return (
      <div> 
        <h1>React lifecycle app</h1>

        <button onClick={() => this.setState({exists: true})} > create </button>
        <button onClick={() => this.setState({exists: false})} > destroy </button>
        <button onClick={() => this.setState({someValue: Math.random() * 100})} > update </button>
        
        {this.state.exists && <Something someValue={this.state.someValue} />}


      </div>
    )
  }
}

export default App