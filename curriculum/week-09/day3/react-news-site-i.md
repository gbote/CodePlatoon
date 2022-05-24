# News Site I

## Topics Covered / Goals
- Planning and creating a React application
- Functional vs class-based components
- Passing down data and functions as props


## Lesson
Today begins a string of lessons involing the 'News Site' project. This is something that we'll be going over together during the lectures for the next few days, as well leave it for you to complete on your own as your daily assignment. The goal of this project is just to understand and get comfortable with using React to develop the front end of a website. 


### Project Setup

- start a basic react project with `npx create react app`
    - `npx` will install and run an npm module if you don't have it, or just run it if you've already installed it
- delete unnecessary boilerplate
- copy data over
    - eventually, we'll use the hackernews API to provide news articles for our app. For now, we'll use some hard-coded sample data in `news.json`. 
- create folder/files for components

### Components
- App: top level component that contains all other components
    - The App tracks all the state for the other components (in this demo).
- ArticleTeaser: a preview of an article, with a headline and a date
    - accepts `id`, `title`, `createdDate`, and `handleTitleClick`
    - accepts a function as a prop. remember the difference between a function call and function reference
- Article: the actual article, with content and images
    - has many props. use spread syntax.
    - conditional rendering. There are a few different ways to do this in react
- AppNav: the navigation bar with links
    - list rendering. create a nav link for each item in the navItems array. 


## Assignments
- [News Site I](https://github.com/romeoplatoon/react-news-site-i)
- [MadLibs](https://github.com/romeoplatoon/react-mad-libs)


