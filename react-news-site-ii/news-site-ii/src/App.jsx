import './App.css';
import { useState } from "react"
import 'bootstrap/dist/css/bootstrap.min.css'

// data
import News from './data/news.json';
import navItemsData from './data/navItems.json';

// components
import AppNav from './components/AppNav/AppNav.jsx';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage'
import ArticlePage from './pages/ArticlePage'

// seed values
const randomArticleIndex = Math.floor(Math.random() * News.length);
const randomArticle = News[randomArticleIndex];

function App() {
  // states
  const [navItems, setNavItems] = useState(navItemsData)
  const [article, setArticle] = useState({
    id: randomArticleIndex,
    title: randomArticle.title,
    abstract: randomArticle.abstract,
    byline: randomArticle.byline,
    image: randomArticle.multimedia.length ? randomArticle.multimedia[0].url : null,
    created_date: randomArticle.created_date
  })

  // renders
  return (
    <div className='app'>
      <AppNav navItems={navItems} handleNavClick={(clickedItem) => { console.log(clickedItem) }} />
      <div className='section'>
      <Router>
          <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/articles/:articleID" element={<ArticlePage />} />
          </Routes>      
      </Router>
      </div>
    </div>
  );
}

export default App;