// console.log('JS read successfully')

// csrf token workaround
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

function addToCart(productId) {
    let data = new FormData()
    data.append('product_id', productId)
    axios.post("/add_to_cart/", data)
        .then(() => {
            console.log("Posted data")
            console.log(data)
        })
        .catch((error)=>{
            console.log('ERROR: ', error)
        })
}