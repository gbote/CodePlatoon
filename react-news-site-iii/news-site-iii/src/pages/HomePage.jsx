import ArticleList from '../components/ArticleList/ArticleList.jsx'
import { useEffect } from 'react';

function HomePage(props) {

  useEffect(() => {
    props.resetArticles()
  }, [])

  return (
    <div>
      <ArticleList articles={props.articles} />
    </div>
  );
}

export default HomePage;
