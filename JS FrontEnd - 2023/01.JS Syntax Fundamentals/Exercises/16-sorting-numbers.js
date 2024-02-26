function solve(arr) {
    let output = [];

   
 // sorting numbers !!!
    let sorted = arr.sort((a,b) => a-b);
    let len = sorted.length;

    for (let i=0; i < len; i+=2) {
        output.push(sorted.shift());
        output.push(sorted.pop())
        }
    return output;
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18]));
