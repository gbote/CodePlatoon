import { useState, useEffect} from 'react'

import './App.css'

import AppNav from './components/AppNav'
import HomePage from './pages/HomePage'
import ArticlePage from './pages/ArticlePage'
import SectionPage from './pages/SectionPage'


import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import axios from 'axios'


function App() {


  const[articles, setArticles] = useState([])
  const[showArticles, setShowArticles] = useState(true)


    async function getData() {
      const date = Math.floor(Date.now() /1000) - 86400
      try{
        const jsonResponse = await axios.get('http://hn.algolia.com/api/v1/search_by_date?', {
          params:{
            tags: ('story'),
            hitsPerPage: 50,
            numericFilters: 'created_at_i<'+date
  
          }
        })
        
        console.log(jsonResponse.data.hits)
        setArticles(jsonResponse.data.hits)
      }
      catch(error){
        console.error('Error occurred fetching data: ', error)
      }

    }

    useEffect( ()=> {
      getData()
    } , [])

  
  return (
    
    <div className="App">
      
      <Router> 
      <AppNav articles={articles} setShowArticles={setShowArticles}/>
        <Routes>
          <Route path='/' element={<HomePage showArticles={showArticles} articles = {articles}/>} />
          <Route path='/articles/:articleID' element={<ArticlePage  articles = {articles} />} />
          <Route path='/sections/:sectionName' element={<SectionPage articles={articles}/> } />

        </Routes>
      </Router>   
      
  
    </div>
  )
}

export default App