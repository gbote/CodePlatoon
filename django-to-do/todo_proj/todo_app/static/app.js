let addData = false;

if (document.getElementById('loginSignupBtn').style.display == 'none') {
  axios.post('/todo/request_todo').then(response=> add_todo_items(response.data.todo_items));
}

const toggleButtons = (email='')=> {
  btnDrop = document.getElementById('btnDrop');
  btnLogSign = document.getElementById('loginSignupBtn');
  if (btnLogSign.style.display == 'none') {
    btnDrop.style.display = 'none';
    btnLogSign.style.display = 'initial';
  }
  else {
    btnLogSign.style.display = 'none';
    document.getElementById('btnGroupDrop1').innerHTML = email;
    btnDrop.style.display = 'initial';
  }
}

const setFocus = (clear=true)=> {
  const todoInput = document.getElementById('todoInput')
  if (clear) todoInput.value = '';
  todoInput.focus();
}
setFocus();

const setEmailFocus = ()=> {
  const inputs = document.getElementsByTagName('input');
  for (const input of inputs) {
    if (input.type == 'email') {
      input.focus();
    }
  }  
}

document.getElementById('loginModal').addEventListener('hidden.bs.modal', function (event) {
  const inputs = document.getElementById('loginModal').getElementsByTagName('input');
  for (const input of inputs) {
    input.value = '';
  }  
  setTimeout(()=> {
    setFocus(false);
    loginSignupBtn = document.getElementById('loginSignupBtn');
    if (loginSignupBtn.style.display == 'none') { // logged  in
      if (addData) add_todo_item(document.getElementById('todoInput').value);
    }
  }, 1);
});

document.getElementById('loginModal').addEventListener('shown.bs.modal', function () {
  setEmailFocus();
  document.getElementById('loginBtn').addEventListener('click', loginClick);
});

document.getElementById('deleteSelected').addEventListener('click', ()=> {
  const inputGroups = document.getElementById('todoGroups').getElementsByClassName('input-group');
  for (const inputGroup of inputGroups) {
    if (inputGroup.firstElementChild.firstElementChild.checked) {
      inputGroup.getElementsByTagName('button')[0].click();
    }
  }
});

document.getElementById('flexSwitchCheckDefault').addEventListener('change', (event)=> {
  const inputGroups = document.getElementById('todoGroups').getElementsByClassName('input-group');
  if (inputGroups.length < 1) event.target.checked = false;
  for (const inputGroup of inputGroups) {
    inputGroup.firstElementChild.firstElementChild.checked = event.target.checked;
  }
  setFocus(false);
});

const checkListEmpty = ()=> {
  const inputGroups = document.getElementById('todoGroups').getElementsByClassName('input-group');
  if (inputGroups.length < 1) document.getElementById('flexSwitchCheckDefault').checked = false;
}

const add_todo_items = todo_items=> {
  todo_items.forEach(todo_item=> {
    createInputGroup(todo_item);
  });
}

const loginClick = ()=> {
  axios.post('/todo/login', {
    email: loginInputEmail.value,
    password: loginInputPassword.value,
  }).then(response=> {
    if (response.data.success) {
      toggleButtons(loginInputEmail.value); 
      add_todo_items(response.data.todo_items)
      document.getElementById('loginCancel').click();
    }
    else alert(response.data.error)
  });
}

const logoutClick = ()=> {
  axios.post('/todo/logout').then(response=> {
    if (response.data.success) {
      todoGroups = document.getElementById('todoGroups');
      todoGroupsBak = todoGroups.cloneNode(false);
      document.getElementById('todoGroups').remove();
      document.getElementById('inputGroup').insertAdjacentElement('afterend', todoGroupsBak);
      toggleButtons();
      setFocus();
    }
    else {
    }
  });  
}

const signupClick = ()=> {
  const signupInputEmail = document.getElementById('signupInputEmail');
  const signupInputPassword = document.getElementById('signupInputPassword');
  const confirmPassword = document.getElementById('confirmPassword');
  let valid = true;
  [signupInputEmail, signupInputPassword, confirmPassword].forEach(input=> {
    if (!input.validity.valid) {
      input.reportValidity();
      valid = false;
    }
  });
  if (valid) {
    axios.post('/todo/signup', {
      email: signupInputEmail.value,
      password: signupInputPassword.value,
    }).then(response=> {
      if (response.data.success) {
        toggleButtons(signupInputEmail.value);
        add_todo_items(response.data.todo_items);
        document.getElementById('signupCancel').click();        
      }
      else alert(response.data.error)
    });
  }
}

const navLinks = document.getElementsByClassName('nav-link')
for (const navLink of navLinks) {
  navLink.addEventListener('shown.bs.tab', ()=> {    
    setEmailFocus();
    const signupInputPassword = document.getElementById('signupInputPassword');
    const confirmPassword = document.getElementById('confirmPassword');
    signupInputPassword.addEventListener('keyup', ()=> {
      confirmPassword.pattern = `^${signupInputPassword.value}$` // validate confirmPassword equals password
    });    
    document.getElementById('signupBtn').addEventListener('click', signupClick);
  });
}  

const createInputGroup = todo_item=> {
  const newGroup = inputGroup.cloneNode(true);
  document.getElementById('todoGroups').insertAdjacentElement('afterbegin', newGroup);
  newGroup.removeAttribute('id');
  const newGroupChildren = newGroup.children;
  for (let i = 0; i < newGroupChildren.length; i++) {
    if (newGroupChildren[i].type == 'text') {
      newGroupChildren[i].removeAttribute('id');
      newGroupChildren[i].value = todo_item.text;
      newGroupChildren[i].disabled = true;
    }
    else if (newGroupChildren[i].type == 'button') {
      delBtn = newGroupChildren[i];
      delBtn.innerHTML = '&#10060';
      delBtn.addEventListener('click', ()=> {
        axios.post('/todo/delete_todo', {
          'todo_item_id': todo_item.id,
        }).then(response=> {
          if (response.data.success) {
            newGroup.remove();
            checkListEmpty();
            setFocus(false)
          }
          else {
            alert(response.data.error);
          }
        });
      });
    }    
    else if (newGroupChildren[i].firstElementChild.type == 'checkbox') newGroupChildren[i].firstElementChild.classList.remove('hidden');
  }
  setFocus(false);
}

const add_todo_item = inputText=> {
  addData = false
  axios.post('/todo/add_todo', {
    text: inputText,
  }).then(response=> {
    if (response.data.success) {
      createInputGroup(response.data.todo_item); 
      setFocus()
    }
    else alert(response.data.error);
  });             
}

document.getElementById('btnAdd').addEventListener('click', event=>{
  inputText = document.getElementById('todoInput').value;
  if (inputText != '') {
    loginSignupBtn = document.getElementById('loginSignupBtn');
    if (loginSignupBtn.style.display != 'none') { // not logged  in
      addData = true;
      loginSignupBtn.click();
      return;
    }  
    add_todo_item(inputText);
  }
});

document.getElementById('inputGroup').addEventListener('keyup', (event)=> {
  if (event.key == 'Enter') {
    document.getElementById('btnAdd').click();
  }
});
