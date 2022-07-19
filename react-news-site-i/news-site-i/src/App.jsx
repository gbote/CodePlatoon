import './App.css';
import { useState } from "react"

// data
import News from './data/news.json';
import navItemsData from './data/navItems.json';

// components
import AppNav from './components/AppNav/AppNav';
import ArticleTeaser from './components/ArticleTeaser/ArticleTeaser'
import Article from './components/Article/Article'

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
      <h1 className="og">AppNav Component</h1>
      <hr />
      <AppNav navItems={navItems} handleNavClick={(clickedItem) => { console.log(clickedItem) }} />

      <h1 className="og">ArticleTeaser Component</h1>
      <hr />
      <ArticleTeaser
        id={article.id}
        title={article.title}
        created_date={article.created_date}
        handleTitleClick={(articleID) => { console.log(articleID) }} />

      <h1 className="og">Article Component</h1>
      <hr />

      <Article {...article} />
    </div>
  );
}

export default App;
