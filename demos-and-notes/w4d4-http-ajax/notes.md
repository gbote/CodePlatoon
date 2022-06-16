# HTTP and AJAX

protocol: the rules by which one piece of software can communicate witha nother


## IP - Internet Protocol
concerned with WHERE a server is located, described by an address called an IP address. 
example ip4v address: 192.0.2.1
currently the web uses IPv4, but there are efforts currently to migrate to IPv6
when you type a domain name into your browser's url bar, your browser must convert that into an IP address. this is done using a network of servers known as the Domain Name System (DNS)


## TCP - Transmission Control Protocol
after we know where something is, TCP is concerned with HOW our data gets there
TCP provides ordered, error-checked delivery of a stream of bytes between applications running hosts that communicate via an IP network
TCP and IP were designed together, so they're often referred to as TCP/IP


## HTTP - hypertext transfer protocol
HTTP describes the format of our application data


## APIs
Application Programming Interface. an API is essentially a contract between two pieces of software that describes how they can interact with each other. most commonly when people say API, they're referring to an HTTP API, that describes what HTTP requests you can send, and what responses you can expect.


## AJAX
by default, sending an HTTP request from a browser unloads the current page, and resets the javascript context
AJAX is a way to send HTTP requests in the background. Asynchronous Javascript and XML
today, we don't commonly use XML data in AJAX requests, instead we use JSON. 
made possible in 1999 in internet explorer, through an object called XMLHttpRequest, or XHR.
nowadays, there is a function called 'fetch' built into the browser that does the same thing as XHR, but with a simpler interface