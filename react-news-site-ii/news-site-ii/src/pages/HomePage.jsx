import { useNavigate } from 'react-router-dom';
import ArticleList from '../components/ArticleList/ArticleList.jsx'
import News from '../data/news.json';

function HomePage(props) {
  // let navigate = useNavigate()

  // function handleTitleClick(event) {
  //   navigate(`/#/articles/${articleID})`)
  // }

  return (
    <div>
      <ArticleList 
        articles={News}
        // handleTitleClick={handleTitleClick}
        // handleTitleClick={(articleID) => {
        // return `props.history.push(/articles/${articleID})` 
        />
    </div>
  );
}

export default HomePage;