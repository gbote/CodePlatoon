// Write unit tests!
var pd = require("./padArray");

tests = [
    {'in1':[1,2,3], 'in2':2, 'in3':null,           'ans':[1,2,3]},
    {'in1':[1,2,3], 'in2':5, 'in3':null,           'ans':[1,2,3,null,null]},
    {'in1':[1,2,3], 'in2':5, 'in3':'apple',        'ans':[1,2,3,'apple','apple']},
    {'in1':[1,2,3], 'in2':0, 'in3':null,           'ans':[1,2,3]},
];

testedFunction = pd.pad;
count = 0;
total = tests.length;

for (let i = 0; i < total; i++) {
  let passed = true;
  testVal1 = testedFunction(tests[i]['in1'],tests[i]['in2'],tests[i]['in3']);
  testVal2 = tests[i]['ans'];
  if (testVal1.length != testVal2.length){
    passed = false;
  } else {
    for (let i = 0; i < testVal1.length; i++) {
        if (testVal1[i] !== testVal2[i]) {
            passed = false; 
        }
    }
  }
  if (passed) {
    console.log(`Passed test ${i+1} of ${total}`);
    count++;
  } else {
    console.log(`Failed test ${i+1} of ${total}`);
  }
}

console.log(`${count}/${total} tests passed.`);