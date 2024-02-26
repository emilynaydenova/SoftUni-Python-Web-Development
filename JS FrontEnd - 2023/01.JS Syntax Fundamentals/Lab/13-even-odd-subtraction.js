
function solve(arr) {
    let evenSum = 0;
    let oddSum = 0;
    let i;
    let len = arr.length;

    for (i = 0; i < len; i += 1) {
        if (arr[i] % 2 == 0) {
            evenSum += arr[i];
        } else {
            oddSum += arr[i];
        }
    }

    console.log(evenSum-oddSum);
}

solve([1, 2, 3, 4, 5, 6]);
solve([3, 5, 7, 9]);
solve([2, 4, 6, 8, 10]);