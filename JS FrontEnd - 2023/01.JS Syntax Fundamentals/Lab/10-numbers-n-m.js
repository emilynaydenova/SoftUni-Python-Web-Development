// m is bigger than n

function solve(m, n) {
  for (let i = m; i >= n; i--) {
    console.log(i);
  }
}

solve(6, 2);
solve(4, 1);

console.log(~~(7 / 3));

let nums = [1, 2, 3, 4]
console.log(nums.slice(-1));

let res = nums.unshift(20,30);
console.log(res);
console.log(nums);