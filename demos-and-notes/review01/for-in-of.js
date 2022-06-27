// for-in loops are an old javascript feature for looping through objects

const alice = {
    name: 'alice',
    age: 34,
    job: 'Historian',
}

// for ( let key in alice ) {
//     console.log(key)
//     console.log(alice[key])
//     console.log('=-=-=-=-=-=')

// }


// for-of loops are a newer addition to javascript for looping through arrays
// other languages would call it a for-in loop, but js already had something similar called for-in

const letters = ['a', 'b', 'c', 'd', 'e']
for (let i = 0 ; i < letters.length; i++ ) {
    console.log(letters[i])
    // letters[i] = 'z'
}
// console.log(letters)
// for ( letter of letters ) {
//     console.log(letter)
// }
// for ( letter in letters ) {
//     console.log(letter)
//     console.log(typeof letter)
//     // console.log(letters[letter])
// }

// js arrays are really just objects
// console.log(typeof {})
// console.log(typeof [])
// console.log(Array.isArray([]))
// console.log(typeof function(){})

// for (let letter of letters.reverse() ) {
//     console.log(letter)
//     letter = 'z'
// }
// console.log(letters)

// all numbers in js are 'truthey', except for 0, which is 'falsey'.
let i = 10;
// while (--i){
    // console.log(i)
// }

// console.log(i--)
// console.log(--i)
// when a primitive value is passed into a function, it is passed by value. modifying the function argument won't modify the original value
// letters.forEach(function(letter){
//     console.log(letter)
//     letter = 'z' // this does nothing
// })
// console.log(letters)

const people = [
    {
        name: 'alice', 
        age: 34,
        job: 'dog walker',
    },
    {
        name: 'bob', 
        age: 87,
        job: 'cat walker',
    },
    {
        name: 'carol', 
        age: 39,
        job: 'philanthropist',
    },
]

// non-primitive types are passed by reference, so we can access the actual object here
people.forEach(function(person){
    person.age++
})
console.log(people)