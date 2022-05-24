// REMEMBER TO PSEUDOCODE
// GAMEPLAN
// First, verify min size <= length
//    if yes, return array
//    if no, begin adding value to array until length = minsize

exports.pad = (array, minSize, value = null) => {
    if (minSize <= array.length){
        return array;
    } else {
        let difference = minSize - array.length;
        while (difference > 0) {
            array.push(value);
            difference--;
        }
    }
    return array;
}
