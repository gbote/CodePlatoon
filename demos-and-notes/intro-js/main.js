var x = 10
// console.log(x - 5)


// console.log(21 % 10)

// console.log(.2 + .1)

var firstPayment = .2
var secondPayment = .1
var firstPaymentPennies = firstPayment * 100
var secondPaymentPennies = secondPayment * 100

var totalPennies = firstPaymentPennies + secondPaymentPennies
var total = totalPennies / 100

// we can put a single quote in our string if we escape it. 
// console.log('Don\\\'t do it!')

// console.log(
// 'line 
//  break'
// )
// console.log(` this is a poem it has multiple lines it has multiple lines it has multiple lines it has multiple lines it has multiple lines it has multiple lines it has multiple lines it has multiple lines it has multiple lines read them all, please `)

// console.log('hello ' + 'world')

var greeting = 'hello'
var place = 'world'
var num = 1
var num2 = 2
// console.log(`${greeting} ${place} ${num + num2}.`)

// javascript must convert the number to a string
// console.log(4 + '4')
// console.log('4' + 4)

// const age = 12
// age = 13

// let age = 12
// age = 13
// console.log(age)


if ( true && true && true && true && false ) {
    console.log("its true!")
}

// if ( false || false || false || true ) {
//     console.log("its true!!")
// }

// console.log(!!true)

// !! can be used to convert a value to boolean
// console.log(!!4)

// i was wearing a hat, and then I took it off
myHat = 'sombrero'
myHat = null

// strict comparison. both values must be the same type, or they're not comparable
// console.log(4 === '4')

// loose comparison. converts types before comparing
// console.log(4 == '4')

// console.log(null == undefined)
// console.log(null === undefined)

// literal array
// const daysOfTheWeek = ['mon', 'tues', 'wed', 'thurs', 'fri']
// console.log(daysOfTheWeek)
// console.log(daysOfTheWeek[3])
// daysOfTheWeek[3] = 'caturday'
// console.log(daysOfTheWeek)

// object literal
const alice = {
    name:'Alice', // keys are assumed to be strings, you don't need ""
    age: 24,
}
const bob = {
    name:'bob', // keys are assumed to be strings, you don't need ""
    age: 43, // trailing comma is optional, but recommended
}
const people = [alice, bob, { name: 'carol', age: 53}]

// console.log(alice.name)

// let randomNumber = Math.random() // random number between 0 and 1


// let property = randomNumber > .5 ? 'age' : 'name'

// 'log alice at property'
// console.log(alice[property])

// this function takes two parameters: first, and last
// console.log(fullName('Dan', 'Stokes'))
// function fullName(first, last){
//     const answer = `${first} ${last}`
//     // console.log(answer)
//     return answer
// }

// this function is being passed two arguments: 'Dan', and 'Stokes'

// doSomething()
// const doSomething = function(){
//     console.log("i did something!")
// }

// arrow functions are more modern, and generally a bit simpler. prefer them to function(){}, unless you need function(){}
const doSomethingElse = (name) => {
    return `${name} did something else!`
}
// console.log(doSomethingElse('Carol'))

const eve = {
    name: 'eve',
    age:22,
    sayHello: ()=>{
        console.log("hello!")
    }
}
// eve.sayHello()
const helloWorld = "Hello world"
helloWorld[3] = 'z' // this does nothing
// console.log(helloWorld[3])
// console.log(greeting.includes('ello'))
// slice gives you a substring from a larger string
// console.log(helloWorld.slice(4, 8))

// copy a string
const otherHello = helloWorld.slice()

const helloArray = helloWorld.split('')
// console.log(helloArray)
helloArray[3] = 'z'
helloArray.push('!')
const helloFinal = helloArray.join('')

// console.log(helloFinal)

const numbers = [1,6,2,8,5,9]
// this is just the indeces. probably a mistake
// for ( key in numbers ) {
//     console.log(key)
// }
// for ( let i = 0; i<numbers.length; i++ ){
//     console.log(numbers[i])
// }
// for ( let num of numbers ) {
//     console.log(num)
//     if ( num ===6 ) { break }
// }

// i dont call this function myself, foreach calls it for me
// numbers.forEach((num)=>{
//     console.log(num)
// })

const malory = {
    name: 'malory',
    age: 32,
}
// for ( let key in malory ) {
//     console.log(key)
//     console.log(malory[key])
//     console.log('-=-=-=-=-=')
// }


const thingsToDo = {
    wakeUp: ()=>{ console.log("wake up!")},
    eatBreakfast:()=>{ console.log("eat breakfast!")},
    age: 4,
}

for (let thing in thingsToDo){
    // console.log(typeof thing)
    if ( typeof thingsToDo[thing] === 'function' ) {
        thingsToDo[thing]()
    }

}

console.log(thing)