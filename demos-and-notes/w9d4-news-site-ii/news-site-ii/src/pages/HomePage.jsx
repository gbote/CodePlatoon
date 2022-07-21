import ArticleList from "../components/AritcleList"


function HomePage ({articles}){
    return (
        <div>
            <ArticleList articles={articles}/>
        </div>
    )
}

export default HomePage