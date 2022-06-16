console.log('hello!')

// axios.get does not return our data immeditaely, it returns an object called a promise, which lets us specify what we want to do onec the request finishes
// .then() also returns a promise, so you can chain .then() or .catch() off of any promise repeatedly
axios.get('https://pokeapi.co/api/v2/pokemon/ditto').then((response)=>{
    // if this code runs, the promise has resolved
    // console.log(response)
    // console.log(response.data.types[0].type.url)
    typeUrl = response.data.types[0].type.url

    // whatever is returned from .then() is passed into the next .then(), wrapped in a promise. .then() always returns a promise
    return axios.get(typeUrl)
}).then((typeData)=>{
    console.log(typeData)
}).catch((error)=>{
    // if this code runs, the promise has been rejected
    console.log('no good: ', error)
})


// sometimes, when we write lots of async code using promises, it can lead to heavily indented code.
// also, you can't use try/catch with promises like they're used above, you must use .catch()


// to use async/await, you must create a function that is labeled as 'async'
const getMon = async () =>{
    // inside of an async function, you can use the await keyword 
    try {

        const response = await axios.get('https://pokeapi.co/api/v2/pokemon/ditto')
        console.log(response)
        const typeUrl = response.data.types[0].type.url
        console.log(typeUrl)
        const typeResponse = await axios.get(typeUrl)
        console.log(typeResponse)
    }
    catch(e){
        console.log(e)
    }
}
getMon()
