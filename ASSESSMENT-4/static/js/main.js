function savePost(){
    title = document.getElementById("newTitle").value
    description = document.getElementById("newDescription").value
    price = document.getElementById("newPrice").value
    seller = document.getElementById("newSeller").value
  
    axios.post("", {title : title, description : description, price : price, seller : seller}).then((response) => {
      window.location.href = "/"
      })
  
  }
  
function editPost(){
  title = document.getElementById("newTitle").value
  description = document.getElementById("newDescription").value
  price = document.getElementById("newPrice").value
  seller = document.getElementById("newSeller").value

  axios.post("", {title : title, description : description, price : price, seller : seller}).then((response) => {
    window.location.href = "/"
    })

}

function deletePost(){
  title = ''
  description = ''
  price = 0
  seller = ''

  axios.post("", {title : title, description : description, price : price, seller : seller}).then((response) => {
    window.location.href = "/"
    })
}

function saveCategory(){
  category_name = document.getElementById("newCategory").value

  axios.post("",{category_name : category_name}).then((response) => {
    window.location.href = "/"
  })

}

function editCategory(){
  category_name = document.getElementById("newName").value

  axios.post("", {category_name : category_name}).then((response) => {
    window.location.href = "/"
    })

}

function deleteCategory(){

  category_name = ''

  axios.post("", {category_name : category_name}).then((response) => {
    window.location.href = "/"
  })
}