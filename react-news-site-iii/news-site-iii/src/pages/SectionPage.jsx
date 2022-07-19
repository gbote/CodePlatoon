import ArticleList from '../components/ArticleList/ArticleList.jsx';
import { useParams } from "react-router-dom";
import { useState } from 'react';
import { useEffect } from 'react';

function ArticlePage(props) {
  const params = useParams()
  let sectionName = params.sectionName

  // effects
  useEffect(() => {
    props.filterArticles((a,b)=>(a===b), 'section', sectionName)
  }, [params])

  useEffect(() => {
    props.filterArticles((a,b)=>(a===b), 'section', sectionName)
  }, [])

  return (
    <div>
      <ArticleList articles={props.articles} />
    </div>
  )
}

export default ArticlePage;