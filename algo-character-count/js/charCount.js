exports.charCount = function(string) {
  let arr = string.split("");
  let result = {};
  for (i = 0; i < arr.length; i++) {
    if (arr[i] in result) {
      result[arr[i]] += 1;
    } else {
      result[arr[i]] = 1;
    }
  }
  return result;
};
