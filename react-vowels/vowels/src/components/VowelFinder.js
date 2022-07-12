function VowelFinder(props) {
    const renderHighlightVowels = () => {
      if (props.word === "") {
        return null;
      }
        
      let elements = [];
      let vowelCount = 0;
  
      for (let i = 0; i < props.word.length; i++) {
        // regex to test for vowel
        let isVowel = (/[aeiou]/i).test(props.word[i]); 
  
        if (isVowel) {
          vowelCount++;
        }
  
        elements.push(
          <span 
            key={`letter-${i}`} 
            className={isVowel ? "highlight" : ""}>{/* add "highlight" class if it's a vowel*/}
              { props.word[i] } 
          </span>
        );
      }
  
      // add vowel count summary
      elements.push(<span> has { vowelCount } vowel{ vowelCount === 1 ? "" : "s"}.</span>);
  
      // return JSX
      return elements; // array of JSX elements (will be unpacked somehow when rendering)
    };
  
    return (
      <div>
        <p>Your word { renderHighlightVowels() }</p>
      </div>
    );
}
  
export default VowelFinder;