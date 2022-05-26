// Your Code Here
const bubbleSort = (array) => {
    var swaps = 0;
    var iterations = 0;
    const n = array.length;
    for (let i = 0; i < n; i++) {
        let swapped = false;
        for (let j = 0; j < n; j++) {
            iterations++;
            if (array[j] < array[j - 1]) {
                let temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
                swapped = true;
                swaps++;
            }
        }
        if (!swapped) {
            break;
        }
    }
    console.log("Swaps: ", swaps);
    console.log("Iterations: ", iterations);
    return array;
};


var sequence = [4, 3, 5, 0, 1, 6];
console.log("Final Result: ", (bubbleSort(sequence)));