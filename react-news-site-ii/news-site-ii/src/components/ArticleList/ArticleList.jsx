import ArticleTeaser from "../ArticleTeaser/ArticleTeaser";

function ArticleList(props) {
 
  return (
    <ul className="article-list">
      {props.articles.map((article, index) => (
         <li key={index} className={index % 2 ? "odd-item" : "even-item"}>
          <ArticleTeaser pageUrl={`/articles/${index+1}`} {...article} id={index + 1} />
        </li>
      ))}
    </ul>
  )
}

export default ArticleList;