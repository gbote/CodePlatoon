console.log('todos page')
const feedbackContainer = document.getElementById('feedback');
const todosList = document.querySelector('.todos-list');

const deleteItem  = (event) => {
  console.log("on click value: ", event.target.value)
  axios.post('/success', {
    delete_todo: event.target.value
  })
  .then((response) => {
    console.log("delete response")
    window.location.href = '/success'
  })
}


document.getElementById('todos-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    axios.post('/success', {
        todo: document.getElementById('todo').value,
        user: document.getElementById('hidden').value,
    }).then((response)=>{
        console.log(response.data)
        if (response.data.success == true) {
            newest_todo = response.data.todo_to_add
            console.log(newest_todo)
            const newestListItem = document.createElement('li')
            todosList.appendChild(newestListItem)
            newestListItem.innerHTML=`
              <p class="list-item-text">${newest_todo}</p>
              <div class="item-buttons">
                <button class="btn delete" onclick="deleteItem(event)" value=${newestListItem}>
                x
                </button>
              </div>
              `
              window.location.href = '/success'
        }
        else {
            feedbackContainer.innerHTML = `<p>To-do cannot be blank.</p>`
        }
    })
})