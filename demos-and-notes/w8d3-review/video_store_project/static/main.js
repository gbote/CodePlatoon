console.log('hello')

function add_customer(event){
    event.preventDefault()

    let new_customer = {}

    for (let i =0 ; i < event.target.length; i++){
        let name = event.target[i].name
        let value = event.target[i].value

        new_customer[name] = value

    }
    axios
        .post('/add-customer/', new_customer)
        .then(function(response) {
            customer = response.data.data

            let list = document.getElementById('list')
            let li = document.createElement('li')

            console.log(customer)

            li.innerHTML= `Customer: ${customer.first_name} ${customer.last_name}`
            console.log(li)
            list.appendChild(li)
            // window.location.href=''      //can be used to refresh page

        })
        .catch((response) => {
            console.log('something went wrong')
        })





}

