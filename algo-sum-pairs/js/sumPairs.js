exports.sumPairs = function(array, num) {
    let answers = [];
    let copyArray = [...array];
    for (x in copyArray) {
      for (y in copyArray) {
        if (x !== y && copyArray[x] + copyArray[y] === num) {
          loopAnswer = [copyArray[x], copyArray[y]];
          answers.push(loopAnswer);
        }
      } 
    }
    if (answers.length < 1) {
      return "unable to find pairs";
    }
    arrayLength = Math.floor(answers.length / 2);
    for (let i = 0; i < arrayLength; i++) {
      answers.pop();
    }
    return answers;
};
