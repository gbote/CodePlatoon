import Article from '../components/Article/Article.jsx'
import News from '../data/news.json';
import { useParams } from "react-router-dom";
import { useState } from 'react';
import { Row, Col } from 'react-bootstrap';

function ArticlePage() {
  const params = useParams()
  let articleIndex = params.articleID -1;
  const [article, setArticle] = useState(News[articleIndex])
  return (
    <Row className="justify-content-center">
      <Col sm={8}>
        { 
          article
            ? <Article {...article} image={ article.multimedia.length ? article.multimedia[2].url:null } />
            : <span>404: Article not found.</span>
        }
      </Col>
    </Row>
  )
}

export default ArticlePage;
