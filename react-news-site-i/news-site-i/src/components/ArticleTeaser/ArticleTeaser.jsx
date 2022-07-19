function ArticleTeaser(props) {
  
  const formatDate = (date) => {
    //2017-02-09T09:30:23-05:00
    const year = date.slice(0,4)
    const month = date.slice(5,7)
    const day = date.slice(8,10)
    const hour = date.slice(11,13)
    const min = date.slice(14,16)
    return `${month}/${day}/${year} - ${hour}:${min}`
    //not ideal formatting rn
  }

  return (
    <div className="section article-teaser__container">
      <a className="link article-teaser__title" href="#" onClick={props.handleTitleClick(props.id)}>
        {props.title}
      </a>
      <p className="article-teaser__p">
        {formatDate(props.created_date)}
      </p>
    </div>
  )
}

export default ArticleTeaser;