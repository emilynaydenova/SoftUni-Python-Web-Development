function solve(arr) {
    if (arr.length > 1) {
        let arrFirst = arr[0];
        let arrLast = arr[arr.length - 1];
        console.log(arrFirst + arrLast);
    }
}

solve([20, 30, 40]);
solve([10, 17, 22, 33]);
solve([11, 58, 69]);