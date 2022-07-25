import ArticleList from "../components/ArticleList"
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'

import { useState, useEffect } from "react"
import ArticleTeaser from "../components/ArticleTeaser"

function HomePage ({articles}){

    const [searchTitle, setSearchTitle] = useState('')
    const [results, setResults] = useState([])
    
    const handleChange = (event) => {
        const value = event.target.value
        console.log(`${value} val changed`)

        setSearchTitle(value)
    }

    useEffect( () => {
        if (searchTitle != ''){
            const filteredArticles = articles.filter(article => article.title.includes(searchTitle))
            setResults(filteredArticles)
        }

    }, [searchTitle])



    return (
        <div>
            <Form >
                <Form.Control
                    type="search"
                    placeholder="Search"
                    aria-label="Search"
                    onChange={(event)=>{handleChange(event)}}
                />
            {/* <Button variant="outline-success ">Search</Button> */}
          </Form>
            <div>
            {
                results
                ? <div >
                    <h2>search results</h2>
                    {results.map((article) => (
                    <ArticleTeaser key={article.id} {...article}/>
                ))}</div>
                : ''
            }
            </div>
            
            <hr/>
            <h2>All Articles</h2>
            <ArticleList articles={articles}/>
        </div>
    )
}

export default HomePage