function binarySearchRecursive(value, arr, start, stop){

  let middle = start + Math.floor((stop-start)/ 2);
  if (stop < start){
    return -1;
  }

  if (arr[middle] == value) {
    return middle;
  } else if (value < middle) {
    return binarySearchRecursive(value, arr, start, middle -1);
  } else if (value > middle) {
    return binarySearchRecursive(value, arr, middle + 1, stop);
  }
}

function binarySearch(value, arr){
  return binarySearchRecursive(value, arr.sort(), 0, arr.length-1);
}