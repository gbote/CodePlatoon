# Deployment

- deployment
    - get the app running on AWS EC2
    - learn some differences between running on local host and a live site

- DNS
    - Domain Name System, a network of databases that translate IP addresses into domain names
    - understand a couple of different types of DNS records (A record, CNAME record)

- HTTPS
    - get a green lock in the URL bar so your website looks secure
    - understand what SSL/TLS are, and the types of attacks it prevents against
    - access 'powerful features' for the front-end that are only available in 'secure contexts', such as geolocation, DeviceOrientation/DeviceMotion, getUserMedia, and WebMIDI



## changes to our django app

- set debug=False in settings.py
- set ALLOWED_HOSTS = ['*']
- set CSRF_TRUSTED_ORIGINS = ['https://websiteurl.com']
- 

we'll use SSH keys to log in to our server
usually created in a pair: private key stays safe on your local machine, public key goes to the server
AWS knows what we're trying to do, so they can generate both keys, put the public key where it belongs, and give us the private key

permissions:

9 total permissions, 3 sets of 3
user: read, write, execute
group: read, write, execute
other: read, write, execute

common DNS records
- an A-record maps a domain name to an IP address
- a CNAME-record maps a domain name to another domain name

SSL - secure socket layer. a protocol for encrypting web traffic
when you apply SSL to HTTP, you get HTTPS

for political/marketing reason, SSL was rebranded as TLS - transport layer security

SSL is not actually used anymore, since TLS is the modern replacement. people still use the term 'SSL certificate' to refer to the key that your server