exports.picker = function(prices) {
    let test_combos = [];
    let test_combos_index = [];
    let max_profit = -Infinity;
    let max_profit_index = 0;
    let profit = -Infinity;
  
    // creating an array of all the possible combos
    for (let i = 0; i < prices.length-1; i++){
      for(let j = i+1; j < prices.length; j++){
        test_combos.push([prices[i], prices[j]]);
        test_combos_index.push([i, j]);
      }
    }
  
    // iterate through combos to find index of max profit
    for (let k = 0; k < test_combos.length; k++){
      profit = test_combos[k][1] - test_combos[k][0];
      if (profit > max_profit){
        max_profit = profit;
        max_profit_index = k;
      }
    }
  
    return test_combos_index[max_profit_index];
}
