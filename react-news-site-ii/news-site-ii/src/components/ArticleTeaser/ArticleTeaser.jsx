import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

function ArticleTeaser(props) {
  
  let navigate = useNavigate()

  function handleTitleClick(event) {
    navigate(`/articles/${props.id}`)
  }

  return (
    <div className="section article-teaser__container">
      <Link to={props.pageUrl}>{props.title}</Link>
      {/* <a className="link article-teaser__title" onClick={(event) => {
        event.preventDefault();
        handleTitleClick(props.id);
      }}>
        { props.title }
      </a> */}
      <p className="article-teaser__p">{ props.created_date }</p>
    </div>
  )
}

export default ArticleTeaser;


// // class-based component equivalent code:
// import React, { Component } from 'react';

// class ArticleTeaser extends Component {
//   render() {
//     const { id, title, created_date: createdDate, handleTitleClick } = this.props;
//     return (
//       <div>
//         <a onClick={ () => handleTitleClick(id) }>{ title }</a>
//         <p>{ createdDate }</p>
//       </div>
//     )
//   }
// }

// export default ArticleTeaser;

