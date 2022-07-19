import { Link } from "react-router-dom";

function ArticleTeaser(props) {
  
  return (
    <div>
      <Link to={props.pageUrl}>{props.title}</Link>
      <p>{props.created_date.substring(0,10)}</p>
    </div>
  )
}

export default ArticleTeaser;


