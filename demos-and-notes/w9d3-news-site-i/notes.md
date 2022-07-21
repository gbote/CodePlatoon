# News Site I

## Topics Covered / Goals
- Planning and creating a react app
- Passing down data and functions as props
- Conditional rendering
- React Bootstrap


## Project Setup:
- create app
- delete boilerplate
- import data
- create components

## Components
- App: track all the state of the other components and contain them
- NavBar: list rendering. create a link for each item
- ArticleTeaser (id, Title, date): render info about article. On click show article
- Article (...): has many props. conditional rendering 

## Notes:

### Methods as props 
- Sending a method by reference: HandleNavBarClick
- Sending a method by reference with parameters: () => HandleNavBarClick(parameter)
- Calling a method: HandleNavBarClick()

### Conditional Rendering in 3 ways:
```
const showArticle = true  //or false
const renderIfShow = ()=>{
        if (showArticle){
          return <Article {...article}/>
        }
    }

return  (
    <div>
        {showArticle ? <Article  {...article}/> : ''}
        {showArticle && <Article {...article}/>} 
        {renderIfShow()}
    </div>
)


```
