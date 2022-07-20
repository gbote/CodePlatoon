function Article (props){

    return(
        <div>
            {props.image ? <img src={props.image.url}/>: <p> image not found</p> } 
        </div>
    )
}
export default Article;