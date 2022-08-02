# RESTful API design

REST - REpresentational State Transfer


naive understanding of REST, maps CRUD onto HTTP verbs
create - POST
read - GET
update - PUT
delete - DELETE


"cookie based applications on the web will never be reliable" - Roy Fielding


In modern practice, REST is a software architectural style for creating scalable web services that make resources available to clients. 
there are many features that make an API 'RESTful'. you don't need to apply all of them at once, if it doesn't make sense.

strike a balance between conforming to expectations, and building an API that fits the specific needs of your application
REST is NOT a specific technology, tool, or library, or even a standardized protocol. 


most basic concept in REST is a resource
- document or an image,
- temporal service (today's weather in las angeles)
- a collection of other resources, e.g. `users`
- resources can be queried or modified using HTTP VERBS
- REST APIs USUALLY represent resources as JSON data. not a defining characteristic, but generally true



## STATELESSNESS
- server does not keep track of clients from one request to the next
- clients must supply all relevant information that the server needs to respond to the request
- in a public REST API, the client must authenticate every request
- the APIs we build wont be completely stateless, because they use cookies. this is not very RESTful, but it's very convenient.


## METHODS 
the most important aspect of an HTTP verb when deciding which one to use is IDEMPOTENCE
in computing, we say that an action is IDEMPOTENT if performing that action once has the same effect as performing it multiple times.

a SAFE HTTP method has the same effect if performed multiple times as if it were not done at all

GET - SAFE and idempotent. a GET request should never have any impact on the server state

PUT - idempotent
PUT /api/users/345 {username:'steve'}

POST - NOT idempotent
POST /api/users {username: 'steve'}

DELETE - idempotent 
DELETE /api/users/345

sometimes when a request fails, we might want to resend it automatically


POST /api/accounts/987/deposit {amount: 200}
PUT /api/accounts/987/ {current_balance: 200000000}


## RESPONSES

An API is considered RESTful if it uses meaningful HTTP response status codes
common responses:

200 OK
Standard response for successful HTTP requests. The actual response will depend on the request method used. In a GET request, the response will contain an entity corresponding to the requested resource. In a POST request, the response will contain an entity describing or containing the result of the action.[8]
201 Created
The request has been fulfilled, resulting in the creation of a new resource.[9]
304 Not Modified (RFC 7232)
Indicates that the resource has not been modified since the version specified by the request headers If-Modified-Since or If-None-Match. In such case, there is no need to retransmit the resource since the client still has a previously-downloaded copy.[24]
403 Forbidden
The request contained valid data and was understood by the server, but the server is refusing action. This may be due to the user not having the necessary permissions for a resource or needing an account of some sort, or attempting a prohibited action (e.g. creating a duplicate record where only one is allowed). This code is also typically used if the request provided authentication by answering the WWW-Authenticate header field challenge, but the server did not accept that authentication. The request should not be repeated.
404 Not Found
The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.
405 Method Not Allowed
A request method is not supported for the requested resource; for example, a GET request on a form that requires data to be presented via POST, or a PUT request on a read-only resource.
500 generic server error

the most important thing is to correctly use the 4XX error codes, so that when clients send a bad request, they have some clue about what they messed up


URLs should have NOUNS, not VERBS. the HTTP VERB should (usually) be sufficient to describe what we want to do. the URL should describe what resource we want to perform that action to.

POST /api/v2/users/ {email: 'jeff@amazon.com', password: 'dragons'}
create a new record in the users collection

GET /api/v2/users/456
retrieve data about a specific user

GET /api/v2/users?city=Chicago
query the entire users collection, but only return records where city=Chicago

PUT  /api/v2/users/345 {username: 'MrJeff'}

DELETE /api/v2/users/345

POST /api/v2/users/345/set-password
sometimes, a RESTful URL might have an 'action' in it. this is an exception to the normal rule of 'nouns, not verbs'


## Caching
a RESTful API should use CACHE-CONTROL headers to instruct the client about what to cache, and for how long
weather data should not be cached at all, since it changes frequently
historical data should be cached indefinitely, since it never changes
other resources will be somewhere in between those extremes


## HATEOAS - Hypermedia as the engine of application state
every response from an API should include links to related actions, so the client can continue exploring the API

IMO not particularly useful
can be a lot of work to set up manually, but some API tools can do this automatically


## WHEN To USE/NOT USE REST?
- use REST to make resources on your server available to clients
- not all HTTP verbs make sense for every resource. only use the ones you need



## Dropbox case study

used to have a route GET `/delta`. it was idempotent. returned information about changes to files
querying `/delta` became too complex, with many query parameters, exceeding the limitations of GET.


solution 1: use POST
POST requests can have bodies, with much larger limits than the query string. 
however, the route itself is SAFE and IDEMPOTENT, although POST is defined to be neither. 

solution 2: use REPORT
REPORT is defined as SAFE and IDEMPOTENT
REPORT requests may contain a body
REPORT is very obscure

```javascript
axios.get()
axios.post()
axios.report() // does not exist
axios({
    url:'website.com',
    method: 'REPORT',
})
```


indeed job board

GET /jobs?company=Microsoft 200 4 hour cache
POST /jobs {title: 'engineer', description:'...', created_date:'...'} 201
PUT /jobs/345 {title: 'engineer'} 200
DELETE /jobs/345 200

library
GET /books?author=Microsoft 200 4 hour cache
POST /books {title: 'engineer', description:'...', created_date:'...'} 201
PUT /books/345 {title: 'engineering'} 200
DELETE /books/345 200

PUT /users/345/return-book {book_id: 876} 200

