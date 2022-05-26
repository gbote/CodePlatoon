// Write your unit tests here

// Factorial
var recur = require("./recursionChallenge");

console.log(recur.factorial(8) === 40320);
console.log(recur.factorial(18) === 6402373705728000);
console.log(recur.factorial(45) === 119622220865480194561963161495657715064383733760000000000);

// Palindrome

console.log(recur.palindrome('racecar') === true);
console.log(recur.palindrome('Noon') === true);
console.log(recur.palindrome('Noon'))
console.log(recur.palindrome('ciVic') === true);
console.log(recur.palindrome('nice') === false);
console.log(recur.palindrome(434) === true);
console.log(recur.palindrome(123) === false);

console.log("The following should be true if you're trying to do the extra portion of this challenge");
console.log(recur.palindrome("Sore was I ere I saw Eros.") === true);
console.log(recur.palindrome("A man, a plan, a canal -- Panama") === true);

// Roman Num

console.log(recur.toRoman(1) === 'I');
console.log(recur.toRoman(3) === 'III');
console.log(recur.toRoman(6) === 'VI');
console.log(recur.toRoman(4) === 'IV');
console.log(recur.toRoman(944) === 'CMXLIV');
console.log(recur.toRoman(150) === 'CL');
console.log(recur.toRoman(1000) === 'M');
console.log(recur.toRoman(444) === 'CDXLIV');