function sumDigits(num) {
    let numStr = num.toString().split('')
    let sum = 0;

    numStr.forEach(item => { sum += Number(item); })
    
    console.log(sum);
}

sumDigits(245678);
sumDigits(97561);
sumDigits(543);