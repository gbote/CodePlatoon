exports.translate = function(word) {
    output = '';
    word.split(' ').forEach((w)=> {
        i = 0;
        is_q = false;
        while ((i < w.length) && ((/[^aeiou]/.test(w[i])) || (w[i] == 'u' && is_q))) {
            (w[i++] == 'q') ? is_q = true : is_q = false;
        }
        output += w.slice(i) + w.slice(0, i) + 'ay ';
    });
    return output.slice(0, -1);
};
