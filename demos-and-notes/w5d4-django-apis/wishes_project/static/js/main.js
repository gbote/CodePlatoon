console.log('hello!')

document.getElementById('pokemon-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    const pokemonName = document.getElementById('pokemon-name').value
    console.log(pokemonName)

    axios.post('/show-me-pokemon', {pokemonName: pokemonName}).then((response)=>{
        console.log('response? ', response)
        document.getElementById('pokemon-image').src = response.data.image_url
    })

    axios.get('/show-me-pokemon')
})

/*
GET /users - returns all users
POST /users - creates a new user
DELETE /users/<user id> - deletes a user
PUT /users/<user id> - updates a user 
*/