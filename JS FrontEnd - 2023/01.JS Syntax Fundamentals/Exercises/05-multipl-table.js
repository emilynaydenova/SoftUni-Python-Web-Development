function multiplyBy10(num) {
    let res = 0;
    for (let i = 1; i <= 10; i++) {
        res = num * i;
        console.log(`${num} X ${i} = ${res}`)
    }
}

multiplyBy10(5);
multiplyBy10(2);