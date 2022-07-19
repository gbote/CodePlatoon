import { useState } from 'react';
import { useParams } from 'react-router-dom';
import Article from '../components/Article/Article.jsx'
import News from '../data/news.json';

const ArticlePage = (props) => {
  const params = useParams()

  let articleIndex = params.articleID - 1;

  const [article, setArticle] = useState(News[articleIndex]);

  return (
    <div className='section'>
      {
        article 
          ? <Article {...article} image={ article.multimedia.length ? article.multimedia[2].url : null} />
          : <span>404: Article not found.</span>
      }
    </div>
  )
}

export default ArticlePage;