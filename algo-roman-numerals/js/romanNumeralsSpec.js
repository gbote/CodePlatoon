var rn = require("./romanNumerals");

console.log(rn.toRoman(1) === 'I');
console.log(rn.toRoman(3) === 'III');
console.log(rn.toRoman(4) === 'IV');
console.log(rn.toRoman(9) === 'IX');
console.log(rn.toRoman(14) === 'XIV');
console.log(rn.toRoman(44) === 'XLIV');
console.log(rn.toRoman(150) === 'CL');
console.log(rn.toRoman(944) === 'CMXLIV');

for (let i = 1; i <= 3999; i++) {
    console.log(i);
    console.log(rn.toRoman(i));
}