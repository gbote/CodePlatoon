var char = require("./charCount");

let result_1 = char.charCount("aaabbc")
console.log(result_1['a'] === 3)
console.log(result_1['b'] === 2)
console.log(result_1['c'] === 1)


let result_2 = char.charCount("an apple a day will keep the doctor away")
console.log(result_2['a'] === 6)
console.log(result_2['e'] === 4)
console.log(result_2['l'] === 3)
console.log(result_2['p'] === 3)
console.log(result_2['w'] === 2)
console.log(result_2['d'] === 2)
console.log(result_2['o'] === 2)
console.log(result_2['t'] === 2)
console.log(result_2['y'] === 2)
console.log(result_2['k'] === 1)
console.log(result_2['h'] === 1)
console.log(result_2['i'] === 1)
console.log(result_2['c'] === 1)
console.log(result_2['n'] === 1)
console.log(result_2['r'] === 1)


