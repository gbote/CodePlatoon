import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'

const element = document.getElementById('my-react-app-root');
const appRoot = ReactDOM.createRoot(element)

appRoot.render(
  <App />
)
