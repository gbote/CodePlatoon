# News Sise II

## Topics Covered / Goals
- Use client side routing / React router
- Understand the Component lifecycle
- React Bootstrap


## Lesson
- News Site II (see assignment list)

### Article list component
> Instead of just viewing one random article, a user should be able to view a list of article teasers, and then click one of them that they want to read. 

> Let's create a component for the home page that will list our articles

```javascript
import "./articleList.css"
import ArticleTeaser from '../ArticleTeaser/ArticleTeaser.js';


function ArticleList(props) {
  return (
    <ul id="articles">
      { 
        props.articles.map((article, index) => (
          <li key={index} className={index % 2 ? "odd-item" : "even-item"}>
            <ArticleTeaser { ...article } id={ index + 1 } />
          </li>
        ))
      }
    </ul>
  )
}

export default ArticleList;
```

### React-router
> When we click a link in our navbar, the page refreshes, and we get a new random article. We need to use react-router so that we can 'change the page' without losing application state. From the server's perspective, we're still on the same page, but to the user, they are moving to different pages on your site. 

> For now, we'll need at least two pages. The home page will have a list of articles, and then we'll have another page for viewing an individual article.

#### hash-router vs browser-router
> Normally, whenever the URL changes, your browser sends a GET request to that new URL. However, by default, if the URL contains a `#`, then anything that changes after the `#` is not considered a new server-side route, and so no data is sent to the server. This is used for client-side routing to elements with a specific id. You can access this information from javascript with `window.location.hash`. hash-router extends this concept, and uses the value of `window.location.hash` to load different components, which will serve as the pages of our website.

> Another option for client-side routing is the browser-router. This approach doesn't leave a `#` in the URL, and instead uses extra javascript to avoid making requests to the server when the URL changes. Using the browser router can cause a variety of bugs to occur in your application, because there will be some situations where client-side URLs will accidentally get sent to the server. When a user refreshes the page or just types a URL directly into the URL bar, that request will go to the server, and your server needs to be prepared to handle that request gracefully. Also, many modern browsers don't even show the full URL by default, so the sole benefit of the browser router is often irrelevant. 


### React-bootstrap
> It's easy to use bootstrap in our react app the same way we have been using it already. We could load bootstrap's CSS and JS in our index.html, and define a react component that uses those bootstrap classes. 

```javascript
function MyButton(props) {
  return (
    <button type="button" class="btn btn-primary">{props.buttonText}</button>
  );
}
```

> There's nothing wrong with this approach, but it turns out that other people have already done this work for us. We can use react-bootstrap to import bootstrap components as pre-built react components, instead of constructing them with HTML. Let's install react-bootstrap (and regular bootstrap) with `npm install react-bootstrap bootstrap`, then let's [read the docs](https://react-bootstrap.github.io/getting-started/introduction) to figure out how to use it. 

## External Resources
- [React Bootstrap](https://react-bootstrap.github.io/getting-started/introduction)

## Assignments
- [News Site II](https://github.com/romeoplatoon/react-news-site-ii)
- [Hangman](https://github.com/romeoplatoon/react-hangman)


