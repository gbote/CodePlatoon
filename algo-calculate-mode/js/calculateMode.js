exports.calculateMode = (arr) => {
    const frequencies = {};
    for (const element of arr) {
      if (!frequencies[element]) {
        frequencies[element] = 0;
      }
      frequencies[element]++;
    }
    return getMaxValues(frequencies);
};
  
const getMaxValues = (frequencies) => {
    return Object.keys(frequencies).filter((x) => {
        return frequencies[x] == Math.max.apply(null, Object.values(frequencies));
    });
};