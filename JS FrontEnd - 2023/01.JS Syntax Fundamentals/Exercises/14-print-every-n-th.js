function solve(arr, step) {

    let selected = []
    let len = arr.length;
    for (let i = 0; i < len; i += step) {
        selected.push(arr[i]);
    }
    return selected;
}


console.log(solve(['5',
    '20',
    '31',
    '4',
    '20'],
    2
));

console.log(solve(['1',
    '2',
    '3',
    '4',
    '5'],
    6
));