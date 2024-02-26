function charsToString(...chars) {
    let concatStr = chars.join('');
    console.log(concatStr);
}

charsToString('a','b','c');
charsToString('%','2','o');
charsToString('1','5','p');

// There are four methods in JavaScript for string concatenation: using the concat() method, using the '+' operator, using the array join() method, and using template literals.