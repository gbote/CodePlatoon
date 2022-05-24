exports.palindrome = function(word) {
    let cleanedArr = word.toString().toLowerCase().split('').filter((character) => /[a-z0-9]/.test(character));
    return cleanedArr.join('') === cleanedArr.reverse().join('');
};
