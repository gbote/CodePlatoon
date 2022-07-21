import { useState } from 'react'

import './App.css'

import NavBar from './components/NavBar'
import HomePage from './pages/HomePage'
import ArticlePage from './pages/ArticlePage'

import NewsData from '../data/news.json'
import NavItemsData from '../data/navItems.json'

import { HashRouter as Router, Routes, Route } from 'react-router-dom';


function App() {

  const[navItems, setNavItems] = useState(NavItemsData)
  const[articles, setArticles] = useState(NewsData.map(( article, index) => {
    return {
      id: index,
      title: article.title,
      abstract: article.abstract,
      byline: article.byline,
      image: article.multimedia.length ? article.multimedia[0] : null,
      created_date: article.created_date
    }})
    )

  const getArticleById = (articleId) => {
    return articles[articleId]
  }
  
  return (
    <div className="App">
      <NavBar items={navItems} />
      
      <Router> 
        <Routes>

          <Route path='/' element={<HomePage articles = {articles}/>} />
          <Route path='/articles/:articleID' element={<ArticlePage  getArticleById={getArticleById} />} />

        </Routes>
      </Router>   
      
      {/* <ArticleList articles={articles}/> */}
  
    </div>
  )
}

export default App