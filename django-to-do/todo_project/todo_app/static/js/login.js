console.log('login?')
const feedbackContainer = document.getElementById('feedback'); 


document.getElementById('login-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    axios.post('/login', {
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
    }).then((response)=>{
        console.log(response.data)
        if (response.data.success == true) {
          console.log('userid', response.data.id)
            window.location.href = '/success'
        }
        else {
            feedbackContainer.innerHTML = `<p class="feedback-text">User does not exist or password is incorrect. Please <a class="feedback-link" href="/sign-up">sign up</a> and log in or try logging in again.</p>`
        }
    })
}) 
