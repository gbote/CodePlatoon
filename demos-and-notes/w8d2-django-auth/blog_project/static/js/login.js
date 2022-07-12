axios.post('/login', {
    email: 'jeffbezos@amazon.com',
    password: 'dragons',
}).then((response)=>{
    console.log(response)
})