import axios from 'axios'

async function fetchArticleById (articleID) {

    let response = await axios.get('http://hn.algolia.com/api/v1/search?', {
        params:{
            tags: 'story_'+articleID
        }
    })
    console.log(response)
    return response

}
const fetchArticlesBySection = (section) => {

}
const fetchArticles = (fitlers = null) => {

}

export {
    fetchArticleById,
    fetchArticlesBySection,
    fetchArticles
}
