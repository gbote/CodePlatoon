// console.log('hello world!')
// console.log(this) // when you're not inside of a function(){}, this refers to the window.


const alice = {
    name: 'alice',
    sayHello: function(){
        // when you access `this` inside of a function(){}, it refers to the object that the function is a property of. 
        console.log(`Hello, my name is ${this.name}.`)
    }
}

// alice.sayHello()

const whatIsThis = function(){
    console.log(this)
}
// whatIsThis()

const bob = {
    name: 'bob',
    sayHello: ()=>{
        // arrow functions don't rebind `this`, so it still refers to the window
        console.log(`My name is ${this.name}.`)
    }
}

// bob.sayHello()

const carol = {
    name: 'carol',
    sayHello: function(){
        setTimeout(function(){
            console.log(`My name is ${this.name}.`)
        })
    }
}
// carol.sayHello()

const dan = {
    name: 'dan',
    sayHello: function(){
        setTimeout(()=>{
            console.log(`My name is ${this.name}.`)
        })
    }
}
// dan.sayHello()

const sayHello = function(){
    console.log(`My name is ${this.name}.`)
}

const eve = {
    name:'eve',
    sayHello: sayHello,
}

// when called as a local variable, this is the window
// sayHello()

// when called as a property of an object, this is the object
// the value of this depends on how the function is CALLED, not how it is defined. 
// eve.sayHello()
// console.log(sayHello === eve.sayHello)


// we're pretending this is a class, so we named it with a capital letter
// const Person = function(name, age){
//     // const this = {} // this happens when you call a function with `new`
//     this.name = name
//     this.age = age
    

//     // console.log('hello!', this)

//     // return this // happens automatically when you call a function with `new`
// }
// Person.prototype.sayHello = function(){
//     console.log(`My name is ${this.name}.`)
// }
// Person.prototype.sayGoodbye = function(){
//     console.log(`See ya later!`)
// }

class Person {
    constructor(name, age){
        this.name = name
        this.age = age
    }
    sayHello(){
        console.log(`Hello, my name is ${this.name}.`)
    }
    sayGoodbye(){
        console.log('see ya later!')
    }
    toString(){
        return `here's ${this.name} as an string: + ${this.name} ${this.age}`
    }
}


// since Person is intended to be used as a constructor function, it must be called with the `new` keyword
const malory = new Person('malory', 32)

// js will first check if sayHello exists on malory herself. if not, js will check her constructor's prototype
malory.sayHello()
// malory.sayGoodbye()
console.log(malory + '!')
// console.log(Person)
// console.log(malory)