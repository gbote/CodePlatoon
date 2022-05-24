// GAMEPLAN:
// Split number string into an array of its elements.
// Iterate backwards through the array as such:
//     For every other number:
//        Double every other number
//        If current number > 9, add 1 to (current number % 10)
//     for each number (odd) or result (even), add to sum total
// Verify sum total mod 10 equals 0

exports.creditCheck = function(str) {

    str = str.split("");
    let even = false;
    let sum = 0;
    let changeNum = 0; 
  
    for (let i = str.length-1; i >= 0; i--) { 
      changeNum = Number(str[i]); 
      if (even) {
        changeNum *= 2;
        changeNum = changeNum > 9 ? (changeNum % 10) + 1 : changeNum;
        even = false;
      } else {
        even = true;
      }
      sum += changeNum;
    }

    return (sum % 10) === 0 ? "The number is valid!" : "The number is invalid!";
}