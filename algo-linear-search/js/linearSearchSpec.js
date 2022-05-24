let ls = require("./linearSearch");

console.log(ls.linearSearch(3, [1,2,3]) === 2);
console.log(ls.linearSearch(1, [1,2,3]) === 0);
console.log(ls.linearSearch(4, [1,2,3]) === undefined);
console.log(ls.linearSearch(13, [1,2,3]) === undefined);

console.log(ls.linearSearchGlobal("a", ["b", "a", "n", "a", "n", "a", "s"])); //answer: [1, 3, 5]
console.log(ls.linearSearchGlobal("s", ["b", "a", "n", "a", "n", "a", "s"])); //answer: [6]
console.log(ls.linearSearchGlobal("n", ["b", "a", "n", "a", "n", "a", "s"])); //answer: [2, 4]