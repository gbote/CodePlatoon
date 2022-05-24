// How can you make this more scalable and reusable later?

const isArmstrong = (num) => {
  const nums = num.toString().split('').map( el => parseInt(el) );
  const power = nums.length;
  let sum = 0;

  for (const el of nums) {
    sum += el ** power;
  }

  return sum === num;
};

exports.findArmstrongNumbers = function(nums) {
  let armstrongNumbers = [];
  for (const num of nums) {
    if (isArmstrong(num)) {
      armstrongNumbers.push(num);
    }
  }
  return armstrongNumbers;
};