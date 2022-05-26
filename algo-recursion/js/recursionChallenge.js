
exports.factorial = function(num) {
    return (num > 1) ? num * this.factorial(num - 1) : 1;
};
  
exports.palindrome = function(word) {
    // formatting string type with no whitespace and lowercase
    if (typeof word === 'string') {
        word = word.replace(/\s+/g,'')
        word = word.replace(/[^a-zA-Z0-9]/g,'')
        word = word.toLowerCase();
    } else {
      word = word.toString();
    }
  
    let i = 0; 
    let j = word.length - 1;
    
    if (word.length === 1){
      return true;
    } else if (word.length == 2){
      if (word[0] === word[1]){
        return true;
      } else { 
        return false;
      }
    } else {
      if (word[0] === word[word.length-1]) { 
        return this.palindrome(word.substring(1, word.length - 1));
      }
      return false;
    }
};
  
exports.bottles = function(num=99) {
    bottleStr = num > 1 ? 'bottles' : 'bottle';  
    if (num > 0){
      console.log(`${num} ${bottleStr}`);
      return this.bottles(num-1);
    } else {
      console.log(`No bottles`);
    }
};
  
const romanArabicModern = [
  {'roman':'M',   'arabic': 1000},
  {'roman':'CM',  'arabic': 900},
  {'roman':'D',   'arabic': 500},
  {'roman':'CD',  'arabic': 400},
  {'roman':'C',   'arabic': 100},
  {'roman':'XC',  'arabic': 90},
  {'roman':'L',   'arabic': 50},
  {'roman':'XL',  'arabic': 40},
  {'roman':'X',   'arabic': 10},
  {'roman':'IX',  'arabic': 9},
  {'roman':'V',   'arabic': 5},
  {'roman':'IV',  'arabic': 4},
  {'roman':'I',   'arabic': 1},
];
  
exports.toRoman = function(num) {
    if (num == 0) { return ''; }
    for (let val of romanArabicModern) {
      divisible = Math.floor(num / val['arabic']);
      if (divisible >= 1) {
            return val['roman'] + this.toRoman(num-val['arabic']);
        }
    }
};