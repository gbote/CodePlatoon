import Sentence from './components/sentence'
import './App.css';

function App() {
  return (
    <div className="App">
      <ol>
      {[...Array(100)].map((item, i) => (
        <li><Sentence key={i}/></li>
      ))}
      </ol>
    </div>
  );
}

export default App;