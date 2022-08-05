import { useState } from 'react'
import { HashRouter, BrowserRouter, Routes, Route } from 'react-router-dom';
import reactLogo from './assets/react.svg'
import './App.css'
import Homepage from './pages/homepage';
import Gradebook from './pages/gradebook';
import AssignmentPage from './pages/assignment_page';

function App() {

  return (
    <div className="App">
      <h1>helloooo</h1>
      <HashRouter>
        <Routes>
          <Route path='/grades' element={<Gradebook/>}/>
          <Route path='/assignments/:id' element={<AssignmentPage/>}/>
          <Route path='' element={<Homepage/>}/>
        </Routes>
      </HashRouter>
    </div>
  )
}

export default App
