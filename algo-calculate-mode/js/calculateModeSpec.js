// Write your own unit tests here!

var cm = require("./calculateMode");
var shallowEqualArrays = require('shallow-equal/arrays');

console.log(shallowEqualArrays(cm.calculateMode([1,1,2,2,2,3,3]), ['2']));  
console.log(shallowEqualArrays(cm.calculateMode([1,2,3,3]), ['3']));
console.log(shallowEqualArrays(cm.calculateMode([4.5, 0, 0]), ['0']));      
console.log(shallowEqualArrays(cm.calculateMode([1.5, -1, 1, 1.5]), ['1.5']));
console.log(shallowEqualArrays(cm.calculateMode([1,1,2,2]), ['1', '2']));
console.log(shallowEqualArrays(cm.calculateMode([1,2,3]), ['1', '2', '3']));      
console.log(shallowEqualArrays(cm.calculateMode(["who", "what", "where", "who"]), ['who']));