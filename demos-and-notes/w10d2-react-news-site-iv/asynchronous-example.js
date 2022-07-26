
// setTimeout(()=>{console.log('hello')}, 5000)
// console.log('other')
// setTimeout(()=> {console.log('there')}, 6000)

// setInterval(()=>{console.log('hello')}, 5000)

// Promise: js construct and it specificies a future value
let hello = () => {
    return new Promise((onSuccess, onFailure) => {
        setTimeout(()=> onSuccess('hello'), 1000)
    })
}
let howAreYou = (result) => {
    console.log(result)
    return new Promise((onSuccess, onFailure) => {

        setTimeout(()=> onSuccess('how are you'), 1000)
    })
}

let howAreYouDoing = (result) => {
    console.log(result)
    return new Promise((onSuccess, onFailure) => {
        setTimeout(()=> onSuccess(''), 1000)
    })
}
let finalResponse = (result) => {
    console.log(result)
    return new Promise((onSuccess, onFailure) => {
        setTimeout(()=> {
            if(result === ''){
                console.log(result, ' nothing?')
                onFailure('no response error')
            }
            else{
                onSuccess(result)
            }
            
        }, 1000)
    })
}



let bye = (error) => {
    console.log(error)
    console.log('bye')
    
}

//// .then chaining
// function greetings() {
//     hello()
//         .then(howAreYou)
//         .then((response) => howAreYouDoing(response))
//         .then(finalResponse)
//         .catch((error) => bye(error))
// } 

//// async / await
async function greetings() {
    try{
        let result = await hello()
        result = await howAreYou(result)
        result = await howAreYouDoing(result)
        return await finalResponse(result)
    }
    catch (error){
        return bye(error)
    }
} 

greetings()
console.log('after greetings call')
// hello()
//     .then((response) => {
//     console.log('in then')
//     console.log('Final response: ' , response)})
//     .then()
