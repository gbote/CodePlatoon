function Feedback({delayedWord, isPalindrome}) {
    return (
      <div>
      {delayedWord !== '' && 
        <div className="feedback__container">
          <h2>The word <span className="highlight">{delayedWord}</span> is {!isPalindrome && <span className="not">not</span>} a palindrome.</h2>
        </div>  
      }
    </div>
    )
  }
  
  export default Feedback