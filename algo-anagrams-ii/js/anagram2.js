const isCharacterMatch = function(string1, string2) {
    let arr1 = string1.toLowerCase().replace(/\s+/g,'').split('');
    let arr2 = string2.toLowerCase().replace(/\s+/g,'').split('');
    let found = false;
  
    for (let i = 0; i < arr1.length; i++) {
      found = false;
      for (let j = 0; j < arr2.length; j++){ 
        if (arr1[i] === arr2[j]) {
          arr2.splice(j,1);
          found = true;
          break;
        }
      }
      if (!found) {
        return false;
      }
    }
    return arr2.length == 0;
};

exports.anagramsFor = function(word, listOfWords) {
    let ans = [];
    for (let i = 0; i < listOfWords.length; i++){
      if (isCharacterMatch(word, listOfWords[i])) { 
        ans.push(listOfWords[i]);
      }
    }
    return ans;
};
