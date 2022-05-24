exports.factorial = function(num) {
    let fac = exports.factorial;
    return (num == 0) ? 1 : num * fac(num-1);
};
