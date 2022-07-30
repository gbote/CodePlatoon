function Output(props){

  const palindromeCheck = (word) => {
    const re = /[\W_]/g;
    let modifiedWord = word.toLowerCase().replace(re, '');
    let reversedWord = modifiedWord.split("").reverse().join("");
    return modifiedWord === reversedWord ? <h4 id="yes">The word <u>{word}</u> is a palindrome.</h4> : <h4 id="no">The word <u>{word}</u> is <i>not</i> a palindrome.</h4>
  }

  return (
     props.word && palindromeCheck(props.word)
  )
}

export default Output