import { Component } from "react"
import Door from "./Door"

class Game extends Component {
  // states
  // const [prizeDoor, /*setPrizeDoor*/] = useState(Math.floor(Math.random() * props.numDoors) + 1)
  // const [result, setResult] = useState(null)
  state = {
    prizeDoor: Math.floor(Math.random() * this.props.numDoors) + 1,
    result: null,
    canOpen: true
  }

  // events
  updateResult = (door) => {
    if (this.state.result !== null)
      return

    this.setState({ result: door === this.state.prizeDoor })
  }

  startNewGame = () => {
    window.location.reload();
  }

  // renders
  renderDoors = () => {
    let doorElements = []
    for (let i = 1; i <= this.props.numDoors; i++) {
      doorElements.push(
        <Door key={i}
          number={i}
          isPrizeDoor={i === this.state.prizeDoor}
          updateResult={this.updateResult}
          result={this.state.result}
        />
      )
    }
    return doorElements
  }

  renderResult = () => {
    if (this.state.result === null)
      return ""
    else
      return (
        this.state.result
          ? <p className="result-win">You got the prize! You win!</p>
          : <p className="result-lose">There is no prize... You lose.</p>
      )
  }

  render() {
    return (
      <div className="center-container" style={{ pointerEvents: this.props.canOpen ? 'none' : 'auto' }}>
        <h3>Want a prize? Choose a door:</h3>
        <div id="door-container">
          {this.renderDoors()}
        </div>
        <div>
          <button className="btn" onClick={this.startNewGame}>New Game</button>
        </div>
        <div>
          {this.renderResult()}
        </div>
      </div>
    )
  }
}

export default Game;