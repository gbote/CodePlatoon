import './App.css';
import { useState } from "react"
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

// data
import navItemsData from './data/sections.json';
import News from './data/news.json';
// components
import AppNav from './components/AppNav/AppNav.jsx';
import HomePage from './pages/HomePage.jsx';
import ArticlePage from './pages/ArticlePage.jsx';
import SectionPage from './pages/SectionPage.jsx';
import { Container } from 'react-bootstrap';

function App() {

  // states
  const [navItems, setNavItems] = useState(navItemsData)
  const [articles, setArticles] = useState(News)

  // event handlers
  const filterArticles = (func, filterType, filterValue=null) => {
    setArticles(News.filter((article) => {return func(article[filterType], filterValue)}))
  }
  const resetArticles = () => {
    setArticles(News)
  }

  // renders
  return (
    <div id="main-body">
      <AppNav navItems={navItems} filterArticles={filterArticles}/>
      <Container id="main-content" className="my-4 p-3">
        <Router>
          <Routes>
            <Route path="/" element={<HomePage articles={articles} resetArticles={resetArticles}/>} />
            <Route path="/sections/:sectionName" element={<SectionPage articles={articles} filterArticles={filterArticles}/>}/>
            <Route path="/articles/:articleID" element={<ArticlePage />} />
          </Routes>
        </Router>
      </Container>
    </div>
  );
}

export default App;
