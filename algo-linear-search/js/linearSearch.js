const arrayToSearchThrough = [];
for (let i = 1; i <= 1000; i++) {
    arrayToSearchThrough.push(i);
}

exports.linearSearch = function(valueToFind, arrayToSearchThrough) {
    for (let i = 0; i < arrayToSearchThrough.length; i++) {
        if (valueToFind === arrayToSearchThrough[i]) {
            return i;
        }
    }
    return undefined;
}

exports.linearSearchGlobal = function(valueToFind, arrayToSearchThrough){
    let valueToFindIndices = [];
    for(let i = 0; i < arrayToSearchThrough.length; i++){
        if(valueToFind === arrayToSearchThrough[i]){
            valueToFindIndices.push(i)
        }
    }
    if (valueToFindIndices.length != 0) {
        return valueToFindIndices;
    } else{
        return undefined;
    }
}