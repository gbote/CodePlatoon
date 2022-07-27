import Form from 'react-bootstrap/Form'
import { useState, useEffect } from "react"


function Search ({articles, setSearchResults}) {

    const [searchTitle, setSearchTitle] = useState('')
    // const [results, setResults] = useState([])
    
    const handleChange = (event) => {
        const value = event.target.value
        console.log(`${value} val changed`)

        setSearchTitle(value)
    }

    useEffect( () => {
        if (searchTitle != ''){     //has something written in search bar

            const filteredArticles = articles.filter(article => article.title.includes(searchTitle))
            setSearchResults(filteredArticles)
            
        }
        else { // nothing written in the search bar

            setSearchResults([])
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
                
            </Form>
            
        </div>
    )
}

export default Search