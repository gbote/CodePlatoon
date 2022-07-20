import { useState } from 'react'

// import './App.css'

import NavBar from './components/NavBar'
import ArticleTeaser from './components/ArticleTeaser'
import Article from './components/Article'
import ArticleGroup from './components/ArticleGroup'

import NewsData from '../data/news.json'
import NavItemsData from '../data/navItems.json'

const randomArticleIndex = 0
const randomArticle = NewsData[randomArticleIndex];

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
  
  return (
    <div className="App">

      <NavBar items={navItems} />

      {articles.map((article) => (
        <ArticleGroup key={article.id} article={article}/>
        ))
      }
      
    </div>
  )
}

export default App
