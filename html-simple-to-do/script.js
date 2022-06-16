function addEntry(evt) {
    evt.preventDefault();
    let list = document.getElementById('to-do'); // Get list
    let input = document.getElementById('new-entry').value; // Get input text
    let entry = document.createElement('li'); // Make new list item
    let check = document.createElement("input");
    check.type = "checkbox";
    check.onclick = strikeEntry.bind(check);
    check.className = "form-check-input me-1";
    entry.className = "list-group-item";
    entry.appendChild(check);
    entry.appendChild(document.createTextNode(input));
    list.appendChild(entry);
  }
  
  function strikeEntry() {
    if (this.checked) {
      this.parentNode.style.textDecoration = "line-through";
    } else {
      this.parentNode.style.textDecoration = "none";
    }
  }