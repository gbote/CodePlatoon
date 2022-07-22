import {fetchArticleByID, fetchArticles} from '../api/ArticlesAPI.jsx'
import axios from 'axios'
// jest.mock('axios') // replaces axios with a mock version


describe('get article from id', ()=>{
    it('should get some article', async ()=>{

        const value =  await fetchArticleByID(30919257)


        expect(value.data.id).toBe(30919257)
        expect(value.data.by).toBe('robbiejs')
    })
})

describe('get articles from topstories', ()=>{
    it('should get a list of all topstories', async ()=>{
        const value = await fetchArticles()


        expect(value.status).toBe(200)

    })
})