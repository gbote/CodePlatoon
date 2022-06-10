// a 'call' is when you execute/invoke a function.  doSomething()
// a stack is an array where you can only add/remove elements to the top


const first = function(){
    console.log('(PUSH) first function executing')
    second()
    console.log('(POP) first function resolving')
}

const second = function(){
    console.log('(PUSH) second function executing')
    third()
    console.log('(POP) second function resolving')
}
const third = function(){
    console.log('(PUSH) third function executing')
    console.log('hello world!')
    throw Error('oops!')
    console.log('(POP) third function resolving')
}

// first()


someLetters = ['a', 'x','j','n','q','o']

// return true if item exists
const findLetter = function(target){
    for (let i = 0; i < someLetters.length; i++) {
        if ( target === someLetters[i] ) {
            return true
        }
    }
    return false
}

// return true if item exists
const findLetterRecursively = function(target, list){
    // base case
    if ( list.length === 0 ) {
        return false
    }

    lastItem = list.pop()
    if ( lastItem === target ) {
        return true
    }
    else {
        findLetterRecursively(target, list)
    }
}


const limitedRecursion = function(calls, maxDepth){
    if ( calls < maxDepth ) {
        // do useful stuff here
        console.log('again!')
        limitedRecursion(calls + 1, maxDepth)
    }
}

limitedRecursion(0, 10)