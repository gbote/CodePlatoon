import "./App.css"
import { useState } from "react"
import MuteButton from "./components/MuteButton.js"

function App() {
  // states
  const [isMuted, setIsMuted] = useState(false);

  // event handlers
  const toggleMute = () => {
    let newMuteState = !isMuted;
    console.log("Setting new mute state value to", newMuteState);
    setIsMuted(newMuteState);
  };

  // render
  return (
    <div className="App">
      <h2>Mute Button App</h2>
      <hr />
      <MuteButton isMuted={ isMuted } toggleMute={ toggleMute } />
    </div>
  );
}

export default App;