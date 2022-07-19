function Article(props) {

  const formatDate = (date) => {
    //2017-02-09T09:30:23-05:00
    const year = date.slice(0,4)
    const month = date.slice(5,7)
    const day = date.slice(8,10)
    return `${month}/${day}/${year}`
  }

  const formatAuthor = (author) => {
    let arrOfWords = author.split(' ')
    const capitalizedArr = arrOfWords.map((word) => (
      word == "and" || word == "AND" 
        ? word.toLowerCase() 
        : 
        word[0].toUpperCase()+word.slice(1).toLowerCase()
    ))
    const properCap = capitalizedArr.join(' ')
    return properCap
  }
 
  return (
    <div className="section article__container">
      <h1 className="article__title">{props.title}</h1>
      <div className="article-details__container">
        <p className="article__date">{formatDate(props.created_date)}</p>
        {props.byline && <h2 className="article__byline">{formatAuthor(props.byline)}</h2>}
      </div>
      {props.image && <img src={props.image} />}
      <p className="article__abstract">{props.abstract}</p>



    </div>
  )
}

export default Article;