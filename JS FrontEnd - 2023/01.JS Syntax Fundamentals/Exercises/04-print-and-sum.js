function solve(start, end) {
    let nums = [];
    let sum = 0;

    for (let i = start; i <= end; i++) {
        nums.push(i);
    }
    console.log(nums.join(' '));

    // nums.forEach(item => { sum += item; })
    sum = nums.reduce((x,y)=>x+y,0);
    console.log(`Sum: ${sum}`)
}

solve(5, 10);
solve(0, 26);
solve(50, 60);

// array.forEach(item => {
//     sum += item;
// });

// let sum = nums.reduce(function(a, b){
    //     return a + b;
    //   });

// array.map(x => sum += x);