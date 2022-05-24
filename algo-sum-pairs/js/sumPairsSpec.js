var sp = require("./sumPairs");
var deepEqualArrays = require('deep-equal');

// Don't forget to add your tests :)
console.log(deepEqualArrays(sp.sumPairs([1, 2, 3, 4, 5, 6], 6), [[1, 5], [2, 4]])); // [[1, 5], [2, 4]]
console.log(deepEqualArrays(sp.sumPairs([1, 2, 3, 4, 5], 9), [[4,5]])); // [[4,5]]
console.log(deepEqualArrays(sp.sumPairs([1, 2, 3, 4, 5], 7), [[2,5], [3,4]])); // [[2,5], [3,4]]
console.log(sp.sumPairs([3, 1, 5, 8, 2], 27) === "unable to find pairs"); // 'unable to find pairs'
console.log(sp.sumPairs([1, 1, 1, 2, 3, 0, 4], 30) === "unable to find pairs") // 'unable to find pairs' 