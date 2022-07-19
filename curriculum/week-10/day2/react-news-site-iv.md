# News Site IV

## Topics Covered / Goals
- Asynchronous JavaScript review
- Working with Promises review
- Using axios

## Lesson
Today, we are going to continue on with our news site project.

First, let's review some terms to get us all on the same page...

**React Component**: A piece of reusable code that returns markup. Each React Component has its own own state and behaviors. A page can consist of one or more React Components. For us, we have a news site that has many components. Our home page has an ArticleList Component that renders a number of ArticleTeaser Components that render Article Components.

**State**: State is a global Javascript Object (or Python Dictionary if you still think in that way) on a particular React Component. It basically keeps track of how things are in that particular Component (e.g., On vs. Off, Selected vs. Not Selected, number of times clicked, etc.). State is private, meaning that it's scoped within a component.

**Props**: Parameters that you pass from a parent Component to a child Components. When you instantiate a new Component on the page, it may or may not take `props`. `props` and `state` are very different!

Now that we've gotten on the same page, let's move forward!

## Getting Data from an API
Up to this point, we've been building our website using static data that exists within our app. Let's first grab our completed `news-site-iii` and keep it nearby. We'll need it soon. We have been importing our News from `/data/news.json` and passing it into our ArticleList component. That's okay for right now, but we want to have dynamic data being fetched from an API. 

Today's challenge isn't going to be a ton of React. Instead it's mostly using JavaScript to connect with an API and use the returned data in our app, presenting in a React Component. Once we get our news data from the external data source (our API), we will put it in our HomePage and ArticleList components.


## Asynchronous Code

Let's take a step back and first talk about what asynchronous code is, why we use it, and how it operates in JavaScript. Let's take a look a the code below:

```javascript
function wait(time_in_ms) {
    let startTime = new Date().getTime();
    while (new Date().getTime() < startTime + time_in_ms);
}

console.log("quebec");

wait(5000); // wait 5 seconds ("doing some work")
console.log("hello");

wait(6000); // wait 6 seconds ("doing some work")
console.log("world");
```

How long will this code take to execute? Answer: 11 seconds. 

But what if we could do some work in parallel (i.e. asynchronously)? Let's take a look at our updated asynchronous code below:

```javascript
function wait(time_in_ms) {
    let startTime = new Date().getTime();
    while (new Date().getTime() < startTime + time_in_ms);
}

console.log("quebec");

let myCallback = () => { console.log("world"); }
setTimeout(myCallback, 6000); // wait 6 seconds ("doing some work"), asynchronously

wait(5000); // wait 5 seconds ("doing some work")
console.log("hello");
```

How long will this code take to execute? Answer: 6 seconds. 

This is because while we're doing some work on the side for 6 seconds, we are able to do some other work in our main execution thread for 5 seconds. 

## Promises
Next, let's talk about Promises. A [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) in JavaScript is a construct that specifies a future returned value. We are guaranteed to get a value back from a Promise, but we don't know when we'll get that value... this is asynchronous behavior! 

Let's take a look at the basic structure of **creating a Promise**:

```javascript
function doSomething() {
    return Math.random() > 0.25; // success rate: 75% 
}

// an example of a Promise that resolves to a string (NOTE: we can return any data type as needed)
let myPromise = new Promise(
    function(onSuccess, onFailure) { 
        let success = doSomething();
        if (success)
            onSuccess("We did our thing!");
        else
            onFailure("There was an error!!!");
    }
)
```

And next, let's take a look at the basic structure of **consuming a Promise**:

```javascript
function doSomething() {
    return Math.random() > 0.25; // success rate: 75% 
}

// creating a Promise
let myPromise = new Promise(
    function(onSuccess, onFailure) { 
        let success = doSomething();
        if (success)
            onSuccess("We did our thing!");
        else
            onFailure("There was an error!!!");
    }
)

// consuming a Promise
let handleSuccess = (msg) => { console.log("SUCCESS:", msg); };
let handleFailure = (msg) => { console.log("FAILURE:", msg); };

myPromise().then(handleSuccess, handleFailure);
```

Asynchronous code can make your code much faster, when you have tasks that are independent of one another and can run in parallel. However, sometimes, you need to complete some tasks in order.

Let's consider a program that simulates some real world action. I think it's a great time to grab some cereal, so let's do it:

```javascript
let pourCereal = () => { 
    console.log("We poured some cereal!");

    let pourMilk = () => { 
        console.log("We poured some milk!");
        console.log("Now we can eat!"); 
    }

    setTimeout(pourMilk, 3000);
}

setTimeout(pourCereal, 3000);
```

Humans tend to not be great at multitasking, so first we must pour some cereal into a bowl, and then we need to pour some milk on top of the cereal. (We can't realisically do both at once.) 

But what if we don't have a clean bowl to use right now? There's another task we have to take care of now:

```javascript
let washDishes = () => { 
    console.log("We washed a bowl and spoon!");
    
    let pourCereal = () => { 
        console.log("We poured some cereal!");
        
        let pourMilk = () => { 
            console.log("We poured some milk!");
            console.log("Now we can eat!"); 
        }
    
        setTimeout(pourMilk, 3000);
    }

    setTimeout(pourCereal, 3000);
}

setTimeout(washDishes, 15000);
```

This works just fine, however notice how our code design is being affected. The more tasks we add here, the mode nested callbacks that we need to add. This is a design that's commonly referred to as [Callback Hell](https://www.geeksforgeeks.org/what-is-callback-hell-in-node-js/). To resolve this callback hell, we can use Promises in JavaScript to update our code:

```javascript
let washDishes = () => { 
    return new Promise((onSuccess, onFailure) => {
        setTimeout(() => onSuccess("We washed a bowl and spoon!"),15000)
    }); 
}

let pourCereal = (result) => { 
    console.log(result);
    return new Promise((onSuccess, onFailure) => {
        setTimeout(() => onSuccess("We poured some cereal!"), 3000)
    }); 
}

let pourMilk = (result) => {
    console.log(result);
    return new Promise((onSuccess, onFailure) => {
        setTimeout(() => onSuccess("We poured some milk!"), 3000)
    });  
}

let eatBreakfast = (result) => { 
    console.log(result);
    console.log("Now we can eat!");
}

let goHungry = (error) => {
    console.log(error)
    console.log("I’m still hungry!!!");
}

washDishes()
    .then(pourCereal, goHungry) 
    .then(pourMilk, goHungry)
    .then(eatBreakfast, goHungry);
```

Notice how we are able to chain Promises together, via the then() method. The then() method gets called once a Promise is resolved (either fulfilled or rejected). The then() method can create another Promise and continue the chain.

You can also write the chain to handle any error with the same handler function, via a catch():

```javascript
// ...from above

washDishes()
    .then(pourCereal) 
    .then(pourMilk)
    .then(eatBreakfast)
    .catch(goHungry); // this catch will handle any onFailure's
```

### Using async-await instead of .then() construct

Instead of using chained then()'s, there's an alternative design that you can employ, using the `async` and `await` keywords in JavaScript. The one caveat is that you need to create a parent async function. Let's take a look:

```javascript
async function prepBreakfast() {
    let washDishes = () => { 
        return new Promise((onSuccess, onFailure) => {
            setTimeout(() => onSuccess("We washed a bowl and spoon!"), 15000)
        }); 
    }

    let pourCereal = (result) => { 
        console.log(result);
        return new Promise((onSuccess, onFailure) => {
            setTimeout(() => onSuccess("We poured some cereal!"), 3000)
        }); 
    }

    let pourMilk = (result) => {
        console.log(result);
        return new Promise((onSuccess, onFailure) => {
            setTimeout(() => onSuccess("We poured some milk!"), 3000)
        });  
    }

    let eatBreakfast = (result) => { 
        console.log(result);
        console.log("Now we can eat!");
    }

    let goHungry = (error) => {
        console.log(error)
        console.log("I’m still hungry!!!");
    }

    try { 
        let result = await washDishes();
        result = await pourCereal(result);
        result = await pourMilk(result);
        return eatBreakfast(result);
    }
    catch(error) {
        return goHungry(error);
    }
}

prepBreakfast();
```

The `await` keyword will make the excution wait for completion before proceeding to the next line. In the case of Promises, `await` will wait until the Promise is resolved and then will proceed. <ins>**Remember: You can only use the `await` keyword in functions that are marked with `async`**</ins> (otherwise you'll get an error). As we've discussed before, JavaScript is a single-threaded programming language so `await` doesn't actually halt (or "block") your entire application's execution. `async` functions behave differently than normal functions, because we are simulating asynchronous execution via `await`. Also, one key thing to remember is that `async` functions actually always return Promises (return values will automatically be converted to Promises!). And to be safe, we should always wrap our awaits in a try-catch in case something goes wrong.

## Axios
Now let's talk about axios, which can be used to retrieve things from web resources. A call to `axios.get` returns a Promise that will resolve to a Response object. We process this [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object to get the data that we expect back from our fetch request.  


```
npm install axios
```

Next, let's test out axios using the hackernews API. Once we've figured out how to query the API for news stories, let's integrate it into our news site project.



## Assignments
- [News Site IV](https://github.com/romeoplatoon/react-news-site-iv)

