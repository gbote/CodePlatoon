exports.caesarCipher = function(string, num) {
    let answer = "",
        shift = 26 - num;
    
    for (let i=0; i < string.length; i++) {
        if (string[i].match(/[a-zA-Z]/g)) {
            if(string[i].match(/[A-Z]/)) {
                answer += String.fromCharCode((string.charCodeAt(i) - shift - 90) % 26 + 90);
            } else {
                answer += String.fromCharCode((string.charCodeAt(i) - shift - 122) % 26 + 122);
            }
        } else {
            answer += string[i];
        }
    }
    return answer;
};