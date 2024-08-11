/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    let binaryString = num.toString(2);
    let complementChars = [];

    for (let i = 0; i < binaryString.length; i++) {
        complementChars.push((binaryString[i] === '0') ? '1' : '0');
    }

    let complementBinary = complementChars.join('');
    return parseInt(complementBinary, 2);
};