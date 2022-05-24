exports.toRoman = function (arab) {
    const romanNumObj = {
      romanNum1: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
      romanNum10: ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
      romanNum100: ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    };
  
    let romFinal = [];
    let counter = 0;
    stringArray = arab.toString().split("");
    // Converts each array element to equivalent roman numeral
    for (x = stringArray.length - 1; x >= 0; x--) {
      if (x == stringArray.length - 1) {
        romFinal[0] = romanNumObj.romanNum1[stringArray[x] - 1];
        counter += 1;
      } else if (x == stringArray.length - 2) {
        romFinal[1] = romanNumObj.romanNum10[stringArray[x] - 1];
        counter += 1;
      } else if (x == stringArray.length - 3) {
        romFinal[2] = romanNumObj.romanNum100[stringArray[x] - 1];
        counter += 1;
      } else {
        romFinal[counter] = "M";
        counter += 1;
      }
    }
    romFinal = romFinal.reverse().join("");
    return romFinal;
  };