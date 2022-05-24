balanceParens = (str) => {
    const noKeep = new Set();
    const parenIndexStack = [];
    let output = '';
  
    for (let i = 0; i < str.length; i++) {
      if (str[i] == '(') {
        parenIndexStack.push(i);
      } else if (str[i] == ')') {
        if (parenIndexStack.length == 0) {
          noKeep.add(i);
        } else {
          parenIndexStack.pop();
        }
      }
    }

    parenIndexStack.forEach(i=> noKeep.add(i))
    str.split('').forEach((e, i)=> {if (!noKeep.has(i)) output += e})
    return output;
}

module.exports = { balanceParens }