function UserInput({word, setWord}) {
  return (
    <input 
    autoFocus 
    type="text"
    placeholder="Enter a word here."
    value={word}
    onChange={(e) => setWord(e.target.value)}
  />
)
}

export default UserInput