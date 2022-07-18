import "./App.css";
import React, { useEffect, useState } from "react";
import Mole from "./components/mole/Mole.jsx";

function App() {
  // states
  const [dens, setDens] = useState(getDensState());
  const [points, setPoints] = useState(0);

  // effects
  // every 15 milsec it calls getDensState so Moles randomly keep appearing
  useEffect(() => {
    function startGame() {
      setInterval(() => {
        setDens(getDensState());
      }, 1500);
    }

    startGame();
  }, []);

  // helpers
  // Create array of 9 that fills each spot with object that randomly sets isMoleVisible
  function getDensState() {
    return new Array(9).fill({}).map(() => {
      return {
        isMoleVisible: [true, false][Math.round(Math.random())],
      };
    });
  }

  // adds point everytime mole gets whacked
  function onMoleWhacked() {
    setPoints(points + 1);
  }

  // renders
  const denElements = dens.map((den, index) => {
    return (
      <Mole onMoleWhacked={ onMoleWhacked } isVisible={den["isMoleVisible"]} key={`mole-${index}`} />
    );
  });

  return (
    <div className="App">
      <h1>WHACK-A-MOLE!</h1>
      <h2>Points: {points}</h2>
      <div className="dens">
        {denElements}
        <div style={{ clear: "both" }}></div>
      </div>
    </div>
  );
}

export default App;