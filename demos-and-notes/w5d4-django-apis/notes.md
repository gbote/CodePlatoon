# Backend APIs

last week: front-end -> API -> front-end
today: front-end -> back-end -> API -> back-end -> front-end

two reasons for sending requests through the backend:
- many APIs require authentication, so we send the request from the backend to keep our private key secret
- some APIs CANNOT be used from the front-end, due to the Same Origin Principle (SOP). An exception to the SOP is cross-origin-resource-sharing (CORS).
    - by default, when you send an AJAX request, browsers only will use responses from servers in the same origin
    - example origin, including protocol (https), subdomain, and tld: https://developer.mozilla.org/
    - a server that is expecting to receive cross-origin requests can set headers on the response (`access-control-allow-origin: *`), meaning that any client is allowed to use the response


## secret management
Don't ever put keys or other secrets in github!
use environment variables to supply credentials to our app