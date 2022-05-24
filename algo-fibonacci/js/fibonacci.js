const fibonacci = (num) => {
    if (num == 0) {
        return 0;
    }

    return (num <= 2) ? 1 : fibonacci(num-1) + fibonacci(num-2);
}

module.exports = {fibonacci}
