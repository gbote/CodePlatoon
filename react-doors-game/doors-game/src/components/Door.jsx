import { Component } from "react";
import GiftImage from "../images/gift.png"

class Door extends Component {
  // states
  state = {
    opened: false
  }

  toggleDoor = () => {
    let newDoorState = !this.state.opened;
    this.setState({ opened: newDoorState })
    this.props.updateResult(this.props.number)
    let doors = document.getElementsByClassName('door')
  }


  // renders  
  getDoorStateStyle = () => {
    return " " + (this.state.opened ? "door-opened" : "door-closed")
  }

  renderImage = () => {
    return this.state.opened && this.props.isPrizeDoor
      ? <img id="image-prize" src={GiftImage} alt="prize" />
      : null
  }

  getStyle = () => {
    if (this.props.result == null) {
      console.log('null', this.props.result)
      return ''
    }
    else {
      console.log('notnull', this.props.result)
      return ' locked'
    }
  }
  render() {
    return (
      <div className={"door " + this.getDoorStateStyle() + this.getStyle()} onClick={this.toggleDoor} >
        <div>Door {this.props.number}</div>
        {this.renderImage()}
      </div >
    )
  }
}

export default Door;