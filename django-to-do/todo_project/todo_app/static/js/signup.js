console.log('signup?')
const feedbackContainer = document.getElementById('feedback'); 

document.getElementById('signup-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    axios.post('/sign-up', {
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
    }).then((response)=>{
      if (response.data.success == true) {
        window.location.href = '/success'
      } else {
        feedbackContainer.innerHTML = `<p class="feedback-text">You must enter a valid email address in the email field. Try again.</p>`
      }
    })
  }
)