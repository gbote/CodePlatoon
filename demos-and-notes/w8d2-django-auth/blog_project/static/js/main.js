console.log('hello!')

axios.post('/signup', {
    email: 'jeffbezos3@amazon.com',
    password: 'dragons',
    username: 'jeffbezos@amazon.com',
}).then((response)=>{
    console.log(response)
})