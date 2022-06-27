const people = [
    {
        name: 'alice', 
        age: 34,
        job: 'dog walker',
    },
    {
        name: 'bob', 
        age: 87,
        job: null,
    },
    {
        name: 'carol', 
        age: 22,
        job: 'philanthropist',
    },
    {
        name: 'dan', 
        age: 22,
        job: 'hacker',
    },
    {
        name: 'eve', 
        age: 32,
        job: 'hacker',
    },
]

let numbers = [1,4,11,22,87,9]
let sortedNumbers = numbers.sort() // sort with no args in js is not very useful
// console.log(sortedNumbers) // alphabetically sorted numbers. probably not what you wanted.

//use < or > to alphabetically compare things
// console.log('aa' < 'ba')


let sortDirection = 1
primarySortCol = 'age'
secondarySortCol = 'job'
sortedPeople = people.slice().sort(function(a,b){
    // console.log(`person a is ${a.name} and person b is ${b.name}`)
    if ( a[primarySortCol] == b[primarySortCol] ) { 
        if ( a[secondarySortCol] > b[secondarySortCol] ) { return sortDirection }
        if ( a[secondarySortCol] < b[secondarySortCol] ) { return -sortDirection }
        if ( a[secondarySortCol] == b[secondarySortCol] ) { return 0 }
    } // returning 0 means we don't care about the relative order of these two items
    if ( a[primarySortCol] == null ) { return 1 } // if 'a' is null, return 1, to indicate 'a' goes after 'b'
    if ( b[primarySortCol] == null ) { return -1 } // if 'b' is null, return -1 to indicate 'b' goes after 'a'
    if ( a[primarySortCol] >  b[primarySortCol] ) { return sortDirection } // returning a positive number means 'a' goes after 'b'
    if ( a[primarySortCol] <  b[primarySortCol] ) { return -sortDirection } // returning a negative number means 'b' goes after 'a'
})
console.log(sortedPeople)
// console.log(people)

// let gimmeFive = function(){
//     return 5
// }

// const five = gimmeFive()

// two types of array methods:
// destructive methods will modify the original array that you call it on, like push() and pop()
// non-destructive methods, such as slice(), map(), and filter(), do not modify the original array, 

// for some weird reason, sort() in javascript will BOTH return a new array, and modify the original array