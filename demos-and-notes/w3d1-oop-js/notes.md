# OOP in JS

- JS doesn't actually have proper OOP 'classes' like other languages. 
- instead, JS has PROTOTYPES, which can be used to define shared behavior of a group of objects
- nobody actually uses prototypes as intended. we will be using prototypes specifically to recreate OOP, like in python.

- oop in js relies on the 'this' keyword, which is similar to 'self' in python. 

- to run a local webserver, cd into the root of the project and type `python -m http.server`. then go to localhost:8000 in your browser. 

- when you access `this` inside of a function, it refers to the object that the function is attached to. 

- there are three built-in functions in javascript called `call`, `apply`, and `bind`, that let you call or redefine an existing function with a forced value for `this`. When working with frameworks, we might define functions that we don't call, but the framework calls for us. since `this` can be rebound to anything, we must read documentation to know how to use `this` in any particular framework. 


# the `new` keyword