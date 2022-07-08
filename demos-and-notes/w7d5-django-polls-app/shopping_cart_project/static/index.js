function add_item(item_id)  {
    
    axios({
        method: 'post',
        url: '/cart-item/',
        data: {
          item_id: item_id
        }
      })
      .then(function (response){
        const elem = document.getElementById(response.data.item_id)
        elem.innerHTML = response.data.item_quantity
      })
    

}