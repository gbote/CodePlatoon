# Cookies and Sessions


## cookies
by default, HTTP is a stateless protocol. we don't know if multiple requests come from the same user. websites remember repeated visitors using cookies:
- a small piece of data that is stored in the user's browser, when it is instructed to do so by the server via the `set-cookie` HTTP response header
- any web technology that can be used to track a user between pages, similarly to using the set-cookie header


when a server responds to a request with the `set-cookie` header, the browser stores the value of that cookie, and sends it back to the same server on repeated visits. 
there are a few important options that you can set on a cookie to change their behavior:

Middleware: functions that run for every request to your server (or every request for some group of requests)

general process for registering a user:
- user sends a POST request to the server with their email/username password
- server generates a random `salt` (string of random characters) which is appended to the user's password
- the salt+password are hashed
- a user object is created and stored in the database. salt+hash are stored in the database in a single column
- (optional) start a session for the user if they don't have one, or associate their existing session with their new account

hashing is different from encryption:
anything that you can ENcrypt, you can DEcrypt, if you have encryption keys, because encryption is a 2way process
hashing is a 1way process. there is no straightforward way to reverse a hash and recover the original value

a hashing algorithm should be fast enough that a user can be logged in relatively quickly, but slow enough that a hacker can't guess a billion passwords in an hour.
a secure hashing algorithm should produce hashes that look similar for all inputs, so a hacker cannot get clues about the password from the hash. 

salting our passwords guarantees that all hashes are unique, and cannot be found in a rainbow table (list of precomputed hashes)